"""
유튜브 채널 전수 분석 스크립트

채널의 모든 영상·쇼츠 메타데이터를 yt-dlp로 수집하고
카테고리 분류, 월별 추이, TOP 영상 등을 엑셀 + 마크다운 요약으로 저장한다.

설치:
    pip install yt-dlp pandas openpyxl

실행:
    python src/youtube_channel_analysis.py https://youtube.com/@theairbnbdataguy
    python src/youtube_channel_analysis.py <채널URL> --limit 50   # 테스트용 일부만

출력:
    output/유튜브_채널_<핸들>.xlsx        (영상목록 / 카테고리별 / 월별 / TOP20 시트)
    output/유튜브_채널_<핸들>_요약.md     (요약 통계)
    output/유튜브_채널_<핸들>_진행중.csv  (중간 저장, 재실행 시 이어서 수집)
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd

try:
    import yt_dlp
except ImportError:
    print("yt-dlp가 없습니다:  pip install yt-dlp")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"

# 카테고리 규칙: (카테고리명, 제목/태그에서 찾을 키워드 정규식)
# 위에서부터 먼저 매칭되는 카테고리를 채택한다.
CATEGORY_RULES = [
    ("A. 무료 강의 시리즈", r"course|part \d|lesson|module|bianchi method|basics|everything (you need|i know)"),
    ("B. 시장 선정/랭킹", r"market|best place|top \d|cities|city|where to (buy|invest)|destroy|easiest|worst"),
    ("C. 매물 분석 튜토리얼", r"airdna|analy[sz]e|analysis|tutorial|how to (find|use|read)|down to the penny|underwrit|valuation"),
    ("D. 운영 최적화/수익", r"pricing|price|amenit|occupancy|revenue|revpar|listing|optimi|booking|guest|automation|host"),
    ("E. 인사이트/트렌드", r"20\d\d|data nobody|truth|secret|mistake|is it still|dead|bust|saturat|regulation"),
    ("F. 사례/브이로그/소식", r"consult|vlog|journey|my (story|plan)|update|becoming|tour|purchas"),
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


def classify(title: str, tags: str) -> str:
    text = f"{title} {tags}".lower()
    for name, pattern in CATEGORY_RULES:
        if re.search(pattern, text):
            return name
    return "G. 기타"


def length_bucket(seconds) -> str:
    if seconds is None:
        return "미상"
    if seconds <= 60:
        return "쇼츠(≤1분)"
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
    df["카테고리"] = [classify(str(t), str(g)) for t, g in zip(df["제목"], df["태그"].fillna(""))]
    df["길이구간"] = df["길이(초)"].apply(length_bucket)
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

    cols = ["제목", "업로드일", "카테고리", "길이구간", "길이(초)", "조회수", "좋아요", "댓글수", "쇼츠", "태그", "URL", "설명"]
    return {"영상목록": df[cols], "카테고리별": by_cat, "월별": by_month, "길이별": by_len, "TOP20": top20}


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
    args = ap.parse_args()

    handle = slug_from_url(args.channel_url)
    OUTPUT_DIR.mkdir(exist_ok=True)
    progress_csv = OUTPUT_DIR / f"유튜브_채널_{handle}_진행중.csv"
    xlsx_path = OUTPUT_DIR / f"유튜브_채널_{handle}.xlsx"
    md_path = OUTPUT_DIR / f"유튜브_채널_{handle}_요약.md"

    df = collect(args.channel_url, args.limit, progress_csv)
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
