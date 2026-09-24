"""
유튜브 채널 전수 분석 스크립트

채널의 모든 영상·쇼츠 메타데이터를 yt-dlp로 수집하고
카테고리 분류, 월별 추이, TOP 영상 등을 엑셀 + 마크다운 요약으로 저장한다.

설치:
    pip install pandas openpyxl tabulate requests
    pip install yt-dlp            # --backend ytdlp 사용 시에만 필요

실행:
    python src/youtube_channel_analysis.py https://youtube.com/@theairbnbdataguy
    python src/youtube_channel_analysis.py <채널URL> --limit 50        # 테스트용 일부만
    python src/youtube_channel_analysis.py <채널URL> --backend ytdlp   # yt-dlp 사용

백엔드:
    innertube (기본) : 유튜브 내부 API(youtubei.googleapis.com)를 직접 호출. 채널 ID 또는 @핸들 필요.
    ytdlp            : yt-dlp 라이브러리 사용 (www.youtube.com 접근 필요)

출력:
    output/유튜브_채널_<핸들>.xlsx        (영상목록 / 카테고리별 / 월별 / TOP20 시트)
    output/유튜브_채널_<핸들>_요약.md     (요약 통계)
    output/유튜브_채널_<핸들>_진행중.csv  (중간 저장, 재실행 시 이어서 수집)
"""

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests

try:
    import yt_dlp
except ImportError:  # innertube 백엔드만 쓸 때는 없어도 된다
    yt_dlp = None

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"

# 카테고리 규칙: (카테고리명, 제목/태그에서 찾을 키워드 정규식)
# 위에서부터 먼저 매칭되는 카테고리를 채택한다. 쇼츠는 별도 규칙(SHORTS_RULES)을 쓴다.
CATEGORY_RULES = [
    ("A. 무료 강의/코스", r"course|part \d|masterclass|workshop|webinar|starter pack|crash course|mini course|blueprint|trust the process"),
    ("E. 세금/재무", r"\btax|depreciation|1031|loophole|beautiful bill|stocks"),
    ("C. 툴 튜토리얼/매물 분석", r"airdna|rentalizer|bnbcalc|tutorial|analy[sz]|analysis|underwrit|comparable|predict|scorecard|how much|will (actually )?make|make(s)? you money|profitab|deal|5 step|4 step|step by step|quickly"),
    ("B. 시장 선정/지역", r"market|saturat|location|city|cities|michigan|poconos|flagstaff|salt lake|louisville|indianapolis|atlanta|st\. augustine|legal|regulation|race"),
    ("D. 운영/리스팅 최적화", r"amenit|photo|pricing|price|ranking|listing|revenue|design|booking|firepit|gameroom|algorithm|upgrade|makeover|compares you|furniture|budget|hostshare|stayamo|fix"),
    ("F. 사례/인터뷰/스토리", r"client|story|how (he|she|this|these|allison|i (found|helped|taught))|made|earned|profiting|interview|chat|w/|best friend|ep\.|series|turns|couple|firefighter|doctor|consult|impressive|announcement|techvestor|expert|master|legend|queen|genuine|kory|brandon|avery|kenny|daniel|jeremy|ceo|founder|data nerds|journey|becoming"),
    ("G. 인사이트/투자 논평", r"lesson|mistake|reason|wealth|rule|survive|saturation|should you|why|wrong|scared|vacation home|creative|boutique|rich|what happens|entrepreneur|landlord|lease|lead|co-host|arbitrage|contract|difficult|importan|cash flowing|cash-flowing"),
]

SHORTS_RULES = [
    ("S1. 어메니티/디자인", r"amenit|design|hot tub|light|feature|build|inch|photograph|speakeasy|game|pool|room|property|properties|airbnb -|makes|home|house|cabin|beautiful|favorite"),
    ("S2. 수익/사례 숫자", r"\$|\d+k|month|year|client|profit|cash|money|deal|revenue|cost"),
    ("S3. 데이터/분석 팁", r"data|analy|tool|airdna|market|strategy|underwrit|research|number|key"),
    ("S4. 의견/소통/일상", r"."),
]


def slug_from_url(url: str) -> str:
    m = re.search(r"@([\w.-]+)", url)
    if m:
        return m.group(1)
    m = re.search(r"/(?:c|channel|user)/([\w-]+)", url)
    return m.group(1) if m else "channel"


def normalize_channel_url(url: str) -> list[str]:
    """영상 탭과 쇼츠 탭을 모두 순회하도록 URL 목록을 만든다."""
    base = url.split("?")[0].rstrip("/")
    for tab in ("/videos", "/shorts", "/streams", "/featured"):
        if base.endswith(tab):
            base = base[: -len(tab)]
    return [f"{base}/videos", f"{base}/shorts"]


def list_video_ids(channel_urls: list[str]) -> list[str]:
    ids: list[str] = []
    opts = {"quiet": True, "extract_flat": True, "skip_download": True, "ignoreerrors": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        for url in channel_urls:
            try:
                info = ydl.extract_info(url, download=False)
            except Exception as e:  # 쇼츠 탭이 없는 채널 등
                print(f"  건너뜀 {url}: {e}")
                continue
            for entry in (info or {}).get("entries", []) or []:
                vid = entry.get("id")
                if vid and vid not in ids:
                    ids.append(vid)
    return ids


def fetch_video(ydl: "yt_dlp.YoutubeDL", vid: str) -> dict | None:
    try:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={vid}", download=False)
    except Exception as e:
        print(f"  실패 {vid}: {e}")
        return None
    if not info:
        return None
    upload = info.get("upload_date")  # YYYYMMDD
    return {
        "video_id": vid,
        "제목": info.get("title"),
        "업로드일": datetime.strptime(upload, "%Y%m%d").date() if upload else None,
        "길이(초)": info.get("duration"),
        "조회수": info.get("view_count"),
        "좋아요": info.get("like_count"),
        "댓글수": info.get("comment_count"),
        "쇼츠": "Y" if (info.get("duration") or 0) <= 60 and "shorts" in (info.get("webpage_url") or "") else "",
        "태그": ", ".join(info.get("tags") or []),
        "설명": (info.get("description") or "")[:1000],
        "URL": f"https://www.youtube.com/watch?v={vid}",
        "채널명": info.get("channel"),
        "구독자수": info.get("channel_follower_count"),
    }



# ---------------------------------------------------------------------------
# InnerTube 백엔드 (youtubei.googleapis.com)
# ---------------------------------------------------------------------------
INNERTUBE = "https://youtubei.googleapis.com/youtubei/v1"
IT_CONTEXT = {"client": {"clientName": "WEB", "clientVersion": "2.20250101.00.00", "hl": "en", "gl": "US"}}
IT_TAB_PARAMS = {"videos": "EgZ2aWRlb3PyBgQKAjoA", "shorts": "EgZzaG9ydHPyBgUKA5oBAA%3D%3D", "streams": "EgdzdHJlYW1z8gYECgJ6AA%3D%3D"}
IT_SESSION = requests.Session()
IT_SESSION.headers.update({"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"})


def it_post(endpoint: str, body: dict, retries: int = 3) -> dict:
    for attempt in range(retries):
        try:
            r = IT_SESSION.post(f"{INNERTUBE}/{endpoint}?prettyPrint=false", json={"context": IT_CONTEXT, **body}, timeout=30)
            if r.status_code == 200:
                return r.json()
            print(f"  HTTP {r.status_code} ({endpoint}) 재시도 {attempt + 1}/{retries}")
        except requests.RequestException as e:
            print(f"  요청 오류 ({endpoint}): {e} 재시도 {attempt + 1}/{retries}")
        time.sleep(2 * (attempt + 1))
    return {}


def walk(obj, key: str):
    """중첩 JSON에서 key를 가진 모든 값을 생성한다."""
    if isinstance(obj, dict):
        if key in obj:
            yield obj[key]
        for v in obj.values():
            yield from walk(v, key)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk(v, key)


def text_of(node) -> str:
    if not node:
        return ""
    if isinstance(node, str):
        return node
    if "simpleText" in node:
        return node["simpleText"]
    if "runs" in node:
        return "".join(r.get("text", "") for r in node["runs"])
    if "content" in node and isinstance(node["content"], str):
        return node["content"]
    return ""


def parse_count(s: str) -> int | None:
    """'12.4K', '1,234', '510 views', 'No views' → 정수"""
    if not s:
        return None
    m = re.search(r"([\d.,]+)\s*([KMB])?", s.replace("\u00a0", " "))
    if not m:
        return 0 if "No" in s else None
    num = float(m.group(1).replace(",", ""))
    mult = {"K": 1e3, "M": 1e6, "B": 1e9}.get(m.group(2) or "", 1)
    return int(num * mult)


def parse_length(s: str) -> int | None:
    """'22:38' / '1:02:15' → 초"""
    if not s or not re.fullmatch(r"[\d:]+", s):
        return None
    parts = [int(p) for p in s.split(":")]
    total = 0
    for p in parts:
        total = total * 60 + p
    return total


def it_resolve_channel(channel_url: str) -> tuple[str, dict]:
    """채널 URL → (browseId, 헤더 메타). @핸들이면 navigation/resolve_url로 변환."""
    m = re.search(r"/channel/(UC[\w-]{22})", channel_url)
    browse_id = m.group(1) if m else None
    if not browse_id:
        handle = "@" + slug_from_url(channel_url)
        res = it_post("navigation/resolve_url", {"url": f"https://www.youtube.com/{handle}"})
        browse_id = next(walk(res, "browseId"), None)
        if not browse_id:
            raise SystemExit(f"채널 ID를 찾지 못했습니다: {channel_url}")
    home = it_post("browse", {"browseId": browse_id})
    md = home.get("metadata", {}).get("channelMetadataRenderer", {})
    header_text = json.dumps(home, ensure_ascii=False)
    subs = re.search(r'"content": "([\d.,]+[KMB]?) subscribers"', header_text)
    nvid = re.search(r'"content": "([\d.,]+[KMB]?) videos"', header_text)
    meta = {
        "채널명": md.get("title"),
        "채널ID": browse_id,
        "설명": md.get("description"),
        "구독자수": parse_count(subs.group(1)) if subs else None,
        "영상수(채널표시)": parse_count(nvid.group(1)) if nvid else None,
    }
    return browse_id, meta


def it_list_videos(browse_id: str) -> dict[str, dict]:
    """영상·쇼츠·라이브 탭을 continuation 끝까지 순회해 {videoId: 기본정보}를 만든다."""
    found: dict[str, dict] = {}
    for tab, params in IT_TAB_PARAMS.items():
        data = it_post("browse", {"browseId": browse_id, "params": params})
        page = 0
        while data:
            page += 1
            new = 0
            for item in walk(data, "richItemRenderer"):
                s = json.dumps(item)
                ids = re.findall(r'"(?:videoId|contentId)": "([\w-]{11})"', s)
                if not ids:
                    continue
                vid = ids[0]
                if vid in found:
                    continue
                badge = re.search(r'"thumbnailBadgeViewModel": \{"text": "([\d:]+)"', s)
                title = ""
                if "shortsLockupViewModel" in item.get("content", item):
                    # 쇼츠: overlayMetadata.primaryText.content 가 제목
                    mt = re.search(r'"primaryText": \{"content": "((?:[^"\\]|\\.)*)"', s)
                    title = json.loads(f'"{mt.group(1)}"') if mt else ""
                else:
                    # 일반 영상: metadata.lockupMetadataViewModel.title.content
                    mt = re.search(r'"lockupMetadataViewModel": \{"title": \{"content": "((?:[^"\\]|\\.)*)"', s)
                    title = json.loads(f'"{mt.group(1)}"') if mt else ""
                    if not title:
                        for t in walk(item, "title"):
                            title = text_of(t)
                            if title:
                                break
                found[vid] = {"video_id": vid, "제목": title, "탭": tab, "길이(초)": parse_length(badge.group(1)) if badge else None}
                new += 1
            token = None
            for c in walk(data, "continuationItemRenderer"):
                token = next(walk(c, "token"), None)
                if token:
                    break
            print(f"  [{tab}] {page}페이지: +{new} (누적 {len(found)})")
            if not token or new == 0:
                break
            data = it_post("browse", {"continuation": token})
            time.sleep(0.3)
    return found


def it_fetch_video(vid: str, base: dict) -> dict:
    """next 엔드포인트로 업로드일·조회수·좋아요·댓글수·설명·태그를 채운다."""
    d = it_post("next", {"videoId": vid})
    row = {**base, "업로드일": None, "조회수": None, "좋아요": None, "댓글수": None, "태그": "", "설명": "", "URL": f"https://www.youtube.com/watch?v={vid}"}
    if not d:
        return row
    for f in walk(d, "factoidRenderer"):
        label = text_of(f.get("label")).lower()
        acc = f.get("accessibilityText", "")
        if "like" in label:
            row["좋아요"] = parse_count(text_of(f.get("value")))
        elif "view" in label:
            row["조회수"] = parse_count(text_of(f.get("value")))
        elif re.fullmatch(r"\d{4}", label):
            try:
                row["업로드일"] = datetime.strptime(acc, "%b %d, %Y").date()
            except ValueError:
                pass
    for p in walk(d, "videoPrimaryInfoRenderer"):
        row["제목"] = text_of(p.get("title")) or row["제목"]
        if row["조회수"] is None:
            row["조회수"] = parse_count(text_of(next(walk(p.get("viewCount", {}), "viewCount"), None)))
        if row["업로드일"] is None:
            dt = text_of(p.get("dateText"))
            m = re.search(r"([A-Z][a-z]{2} \d{1,2}, \d{4})", dt)
            if m:
                row["업로드일"] = datetime.strptime(m.group(1), "%b %d, %Y").date()
        break
    for sec in walk(d, "videoSecondaryInfoRenderer"):
        row["설명"] = (text_of(sec.get("attributedDescription")) or "")[:1000]
        break
    for h in walk(d, "engagementPanelTitleHeaderRenderer"):
        if "comment" in text_of(h.get("title")).lower():
            row["댓글수"] = parse_count(text_of(h.get("contextualInfo")))
            break
    # next 응답의 lengthText는 추천 영상 것이므로 쓰지 않는다 (쇼츠는 길이 미상으로 둔다)
    row["쇼츠"] = "Y" if base.get("탭") == "shorts" else ""
    return row


def collect_innertube(channel_url: str, limit: int | None, progress_csv: Path) -> tuple[pd.DataFrame, dict]:
    browse_id, meta = it_resolve_channel(channel_url)
    print(f"채널: {meta['채널명']} ({browse_id}) 구독자 {meta['구독자수']} / 영상 {meta['영상수(채널표시)']}")
    done: dict[str, dict] = {}
    if progress_csv.exists():
        prev = pd.read_csv(progress_csv)
        done = {r["video_id"]: r for r in prev.to_dict("records")}
        print(f"이어서 수집: 이미 {len(done)}개 완료")
    print("영상 목록 조회 중...")
    listing = it_list_videos(browse_id)
    ids = list(listing)
    if limit:
        ids = ids[:limit]
    print(f"총 {len(ids)}개 영상 상세 수집")
    rows = list(done.values())
    for i, vid in enumerate(ids, 1):
        if vid in done:
            continue
        row = it_fetch_video(vid, listing[vid])
        row["채널명"] = meta["채널명"]
        row["구독자수"] = meta["구독자수"]
        rows.append(row)
        print(f"  [{i}/{len(ids)}] {str(row['제목'])[:60]}  {row['업로드일']}  조회 {row['조회수']}")
        if i % 10 == 0:
            pd.DataFrame(rows).to_csv(progress_csv, index=False)
        time.sleep(0.2)
    df = pd.DataFrame(rows)
    df.to_csv(progress_csv, index=False)
    return df, meta


def classify(title: str, tags: str, is_short: bool = False) -> str:
    text = f"{title} {tags}".lower()
    for name, pattern in SHORTS_RULES if is_short else CATEGORY_RULES:
        if re.search(pattern, text):
            return name
    return "S4. 의견/소통/일상" if is_short else "H. 기타"


def length_bucket(seconds, is_short: bool = False) -> str:
    if is_short or (seconds is not None and seconds <= 60):
        return "쇼츠(≤1분)"
    if seconds is None or pd.isna(seconds):
        return "미상"
    if seconds <= 600:
        return "단편(1~10분)"
    if seconds <= 1800:
        return "중편(10~30분)"
    return "장편(30분+)"


def collect(channel_url: str, limit: int | None, progress_csv: Path) -> pd.DataFrame:
    done: dict[str, dict] = {}
    if progress_csv.exists():
        prev = pd.read_csv(progress_csv)
        done = {r["video_id"]: r for r in prev.to_dict("records")}
        print(f"이어서 수집: 이미 {len(done)}개 완료")

    print("영상 목록 조회 중...")
    ids = list_video_ids(normalize_channel_url(channel_url))
    if limit:
        ids = ids[:limit]
    print(f"총 {len(ids)}개 영상")

    rows = list(done.values())
    opts = {"quiet": True, "skip_download": True, "ignoreerrors": True, "no_warnings": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        for i, vid in enumerate(ids, 1):
            if vid in done:
                continue
            row = fetch_video(ydl, vid)
            if row:
                rows.append(row)
                print(f"  [{i}/{len(ids)}] {row['제목'][:60]}  조회 {row['조회수']}")
            if i % 10 == 0:
                pd.DataFrame(rows).to_csv(progress_csv, index=False)
    df = pd.DataFrame(rows)
    df.to_csv(progress_csv, index=False)
    return df


def analyze(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    df = df.copy()
    df["업로드일"] = pd.to_datetime(df["업로드일"], errors="coerce")
    df["카테고리"] = [classify(str(t), str(g), sh == "Y") for t, g, sh in zip(df["제목"], df["태그"].fillna(""), df["쇼츠"].fillna(""))]
    df["길이구간"] = [length_bucket(sec, sh == "Y") for sec, sh in zip(df["길이(초)"], df["쇼츠"].fillna(""))]
    df["연월"] = df["업로드일"].dt.to_period("M").astype(str)
    df = df.sort_values("업로드일", ascending=False)

    by_cat = (
        df.groupby("카테고리")
        .agg(영상수=("video_id", "count"), 평균조회수=("조회수", "mean"), 합계조회수=("조회수", "sum"), 평균길이초=("길이(초)", "mean"))
        .round(0)
        .reset_index()
    )
    by_month = (
        df.groupby("연월").agg(업로드수=("video_id", "count"), 합계조회수=("조회수", "sum"), 평균조회수=("조회수", "mean")).round(0).reset_index()
    )
    by_len = (
        df.groupby("길이구간").agg(영상수=("video_id", "count"), 평균조회수=("조회수", "mean"), 평균좋아요=("좋아요", "mean")).round(0).reset_index()
    )
    top20 = df.sort_values("조회수", ascending=False).head(20)[["제목", "업로드일", "조회수", "좋아요", "댓글수", "카테고리", "길이구간", "URL"]]
    df["형식"] = df["쇼츠"].fillna("").map(lambda x: "쇼츠" if x == "Y" else "롱폼")
    df["연도"] = df["업로드일"].dt.year
    by_year = (
        df.groupby(["연도", "형식"]).agg(업로드수=("video_id", "count"), 합계조회수=("조회수", "sum"), 평균조회수=("조회수", "mean"), 중앙값조회수=("조회수", "median")).round(0).reset_index()
    )

    cols = ["제목", "업로드일", "형식", "카테고리", "길이구간", "길이(초)", "조회수", "좋아요", "댓글수", "태그", "URL", "설명"]
    return {"영상목록": df[cols], "카테고리별": by_cat, "연도별": by_year, "월별": by_month, "길이별": by_len, "TOP20": top20}


def write_summary(sheets: dict[str, pd.DataFrame], df: pd.DataFrame, handle: str, path: Path) -> None:
    videos = sheets["영상목록"]
    first, last = videos["업로드일"].min(), videos["업로드일"].max()
    subs = df["구독자수"].dropna().max() if "구독자수" in df else None
    lines = [
        f"# @{handle} 채널 정량 요약",
        "",
        f"- 수집일: {datetime.now():%Y-%m-%d}",
        f"- 채널명: {df['채널명'].dropna().iloc[0] if df['채널명'].notna().any() else '-'}",
        f"- 구독자수: {int(subs):,}" if pd.notna(subs) else "- 구독자수: 미상",
        f"- 영상 수: {len(videos):,}",
        f"- 업로드 기간: {first:%Y-%m-%d} ~ {last:%Y-%m-%d}" if pd.notna(first) else "- 업로드 기간: 미상",
        f"- 총 조회수: {int(videos['조회수'].sum()):,}",
        f"- 영상당 평균 조회수: {int(videos['조회수'].mean()):,}",
        f"- 중앙값 조회수: {int(videos['조회수'].median()):,}",
        "",
        "## 연도별 (롱폼/쇼츠)",
        sheets["연도별"].to_markdown(index=False),
        "",
        "## 카테고리별",
        sheets["카테고리별"].to_markdown(index=False),
        "",
        "## 길이별",
        sheets["길이별"].to_markdown(index=False),
        "",
        "## 조회수 TOP 20",
        sheets["TOP20"][["제목", "업로드일", "조회수", "카테고리"]].to_markdown(index=False),
        "",
        "## 월별 업로드 (최근 24개월)",
        sheets["월별"].tail(24).to_markdown(index=False),
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description="유튜브 채널 전수 분석")
    ap.add_argument("channel_url")
    ap.add_argument("--limit", type=int, default=None, help="테스트용: 앞에서 N개만 수집")
    ap.add_argument("--backend", choices=["innertube", "ytdlp"], default="innertube")
    args = ap.parse_args()

    handle = slug_from_url(args.channel_url)
    OUTPUT_DIR.mkdir(exist_ok=True)
    progress_csv = OUTPUT_DIR / f"유튜브_채널_{handle}_진행중.csv"
    xlsx_path = OUTPUT_DIR / f"유튜브_채널_{handle}.xlsx"
    md_path = OUTPUT_DIR / f"유튜브_채널_{handle}_요약.md"

    if args.backend == "ytdlp":
        if yt_dlp is None:
            sys.exit("yt-dlp가 없습니다:  pip install yt-dlp")
        df = collect(args.channel_url, args.limit, progress_csv)
    else:
        df, _meta = collect_innertube(args.channel_url, args.limit, progress_csv)
    if df.empty:
        print("수집된 영상이 없습니다.")
        sys.exit(1)

    sheets = analyze(df)
    with pd.ExcelWriter(xlsx_path, engine="openpyxl") as writer:
        for name, sheet in sheets.items():
            sheet.to_excel(writer, sheet_name=name, index=False)
            ws = writer.sheets[name]
            for col_cells in ws.columns:
                width = min(60, max(10, max(len(str(c.value or "")) for c in col_cells) + 2))
                ws.column_dimensions[col_cells[0].column_letter].width = width
    write_summary(sheets, df, handle, md_path)
    print(f"\n완료: {xlsx_path}\n      {md_path}")


if __name__ == "__main__":
    main()
