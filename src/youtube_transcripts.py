"""
유튜브 영상 자막(스크립트) 일괄 추출

youtube_channel_analysis.py가 만든 진행중 CSV(또는 영상 ID 목록)를 읽어
영상별 자막을 텍스트로 저장한다. 로컬 PC처럼 www.youtube.com 접근이 되는 환경에서 실행한다.

설치:
    pip install youtube-transcript-api pandas openpyxl

실행:
    python src/youtube_transcripts.py                       # 롱폼 전체
    python src/youtube_transcripts.py --ids l5YN175M1zs,J1s4d3CQUD4   # 지정 영상만
    python src/youtube_transcripts.py --min-views 1000      # 조회수 1000 이상 롱폼만

출력:
    output/transcripts/<video_id>.txt
    output/유튜브_자막_theairbnbdataguy.xlsx  (제목, 업로드일, 조회수, 자막 전문)
"""

import argparse
import sys
from pathlib import Path

import pandas as pd

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    sys.exit("youtube-transcript-api가 없습니다:  pip install youtube-transcript-api")

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"
TRANSCRIPT_DIR = OUTPUT_DIR / "transcripts"


def fetch(video_id: str, languages=("en", "ko")) -> str | None:
    try:
        api = YouTubeTranscriptApi()
        tr = api.fetch(video_id, languages=list(languages))
        return " ".join(seg.text.replace("\n", " ") for seg in tr)
    except Exception as e:  # 자막 없음, 비공개 등
        print(f"  자막 없음 {video_id}: {type(e).__name__}")
        return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=str(OUTPUT_DIR / "유튜브_채널_theairbnbdataguy_진행중.csv"))
    ap.add_argument("--ids", default=None, help="쉼표로 구분한 video_id 목록")
    ap.add_argument("--min-views", type=int, default=0)
    ap.add_argument("--include-shorts", action="store_true")
    args = ap.parse_args()

    TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(args.csv)
    if args.ids:
        wanted = [x.strip() for x in args.ids.split(",") if x.strip()]
        df = df[df["video_id"].isin(wanted)]
    else:
        if not args.include_shorts and "탭" in df:
            df = df[df["탭"] != "shorts"]
        if args.min_views:
            df = df[pd.to_numeric(df["조회수"], errors="coerce").fillna(0) >= args.min_views]
    df = df.sort_values("조회수", ascending=False)
    print(f"{len(df)}개 영상 자막 추출")

    rows = []
    for i, r in enumerate(df.itertuples(index=False), 1):
        out = TRANSCRIPT_DIR / f"{r.video_id}.txt"
        if out.exists():
            text = out.read_text(encoding="utf-8")
        else:
            text = fetch(r.video_id)
            if text:
                out.write_text(text, encoding="utf-8")
        print(f"  [{i}/{len(df)}] {str(r.제목)[:60]}  {len(text.split()) if text else 0} words")
        rows.append({"video_id": r.video_id, "제목": r.제목, "업로드일": r.업로드일, "조회수": r.조회수, "단어수": len(text.split()) if text else 0, "자막": text or ""})

    xlsx = OUTPUT_DIR / "유튜브_자막_theairbnbdataguy.xlsx"
    pd.DataFrame(rows).to_excel(xlsx, index=False)
    print(f"완료: {xlsx}  (개별 파일: {TRANSCRIPT_DIR}/)")


if __name__ == "__main__":
    main()
