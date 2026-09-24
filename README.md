# 에어비앤비 한옥 분석

## 프로젝트 목적

도이옥(한옥 숙박업) 사업을 위한 **서울 한옥 에어비앤비 경쟁 분석**.
서울 5개 구(종로·중·성북·동대문·서대문)에 등록된 한옥 숙소를 전수조사하여
가격, 예약률, 후기 등 운영 현황을 파악한다.

## 폴더 구조

```
에어비앤비 분석/
├── src/                  ← 소스 코드
│   ├── step1_survey.py       Step 1: 한옥 숙소 목록 전수조사
│   ├── step2_data.py         Step 2: 숙소별 상세 데이터 수집
│   ├── airbnb_scraper.py     초기 통합 스크래퍼 (참고용)
│   └── youtube_channel_analysis.py  유튜브 채널 전수 분석 (yt-dlp)
├── output/               ← 수집 결과물
│   ├── 한옥_목록.xlsx        Step 1 결과
│   ├── 한옥_분석.xlsx        Step 2 결과
│   ├── airbnb_*.xlsx         전체/한옥 필터링 데이터
│   └── 유튜브_채널분석_*.md   벤치마킹 채널 분석 보고서
├── dashboard/            ← 시각화
│   └── index.html            한옥 스테이 레이더 대시보드
├── _debug_archive/       ← 디버그 파일 (gitignore)
├── Step1_프로젝트_지침.md
└── 스크래퍼_실행.bat
```

## 워크플로우

```
Step 1 (src/step1_survey.py)
  → 서울 80개 행정동을 검색하여 한옥 숙소 목록 수집
  → 출력: output/한옥_목록.xlsx

Step 2 (src/step2_data.py)
  → 한옥_목록.xlsx의 각 숙소별 상세 데이터 수집
  → 호스트 정보, 예약률, 후기, 가격 등
  → 출력: output/한옥_분석.xlsx

Dashboard (dashboard/index.html)
  → 수집 데이터를 시각화하는 웹 대시보드
```

## 유튜브 채널 벤치마킹

```
python src/youtube_channel_analysis.py https://youtube.com/@theairbnbdataguy
  → 채널의 모든 영상/쇼츠 메타데이터 수집 (yt-dlp)
  → 카테고리·월별·길이별·TOP20 정량 분석
  → 출력: output/유튜브_채널_<핸들>.xlsx, output/유튜브_채널_<핸들>_요약.md
```

분석 보고서: `output/유튜브_채널분석_theairbnbdataguy.md` (523편 전수 데이터 기반)
필요 패키지: `pip install pandas openpyxl tabulate requests` (yt-dlp 백엔드 사용 시 `yt-dlp` 추가)
