# 유튜브 채널 분석 — The Airbnb Data Guy (@theairbnbdataguy)

- 분석 대상: https://youtube.com/@theairbnbdataguy (채널 ID `UCHnwvtvqsfFG2S1d5x5B4HQ`)
- 수집일: 2026-09-24 (채널 전체 523편 전수 수집, `src/youtube_channel_analysis.py`)
- 원본 데이터: `output/유튜브_채널_theairbnbdataguy.xlsx` (영상목록 / 카테고리별 / 연도별 / 월별 / 길이별 / TOP20 시트)
- 분석 목적: 도이옥(한옥 스테이) 사업 관점에서 STR(단기임대) 데이터 교육 채널의 콘텐츠 구조·성과 패턴·수익 모델 벤치마킹

---

## 1. 채널 개요

| 항목 | 실측값 |
|------|--------|
| 채널명 | John Bianchi (브랜드명: The Airbnb Data Guy) |
| 운영자 | John Bianchi — STR Search 창업자 (전 Point Analytics) |
| 구독자 | 12,400명 |
| 총 영상 | 523편 (롱폼 179편 + 쇼츠 344편, 라이브 9편 포함) |
| 총 조회수 | 667,877회 (롱폼 310,772 / 쇼츠 357,105) |
| 영상당 조회수 | 평균 1,277회, 중앙값 751회 (롱폼 중앙값 850 / 쇼츠 642) |
| 첫 업로드 | 2020-03-16 ("My AirDNA 5 Step Process to $100,000 a Year Airbnbs") |
| 최근 업로드 | 2026-09-22 (쇼츠 "Day 4 Cash to Cashflow") |
| 참여율 (좋아요/조회) | 롱폼 2.97%, 쇼츠 2.53% |
| 타 SNS | Instagram 4.6만 / TikTok 2.99만 팔로워 (같은 핸들) |
| 채널 설명 | "Airbnb 투자자가 현명한 매입 결정을 내리고, 수익 안 나는 매물을 사지 않도록 돕는다. 40시간 이상의 무료 코스 제공" |

**한 줄 평가**: 구독자 1.2만의 소형 채널이지만, "Airbnb × 데이터"라는 좁은 니치에서 6년 반 동안 523편을 쌓아 별명(The Airbnb Data Guy) 자체가 검색어가 된 **B2C 리드 생성형 전문가 채널**. 유튜브 자체 수익보다 STR Search 서비스(매물 발굴 대행)로의 퍼널이 목적이며, 롱폼 설명란의 97%에 strsearch.com 링크가 들어간다.

### 운영자 배경 (채널 스토리텔링의 뼈대)
- 2017년, 24세에 금융 자문가를 그만두고 시카고에서 에어비앤비 **임차 재임대(rental arbitrage)** 시작, 시카고·스코츠데일 10~15개 객실 운영
- 운영 중 만든 "수익 나는 매물 찾는 데이터 프로세스"를 상품화 → Point Analytics(시장 리포트 "Profit Map") → **STR Search**(매물 매칭 서비스)
- 실적 클레임: 200개 이상 매물 매입 지원, 누적 9,000만 달러 투자 유도, 현금흐름 500만 달러 이상

---

## 2. 채널 성장 타임라인 (연도별 실측)

| 연도 | 롱폼 편수 | 롱폼 평균조회 | 쇼츠 편수 | 쇼츠 평균조회 | 단계 |
|------|----------|--------------|----------|--------------|------|
| 2020 | 8 | 1,174 | 4 | 662 | 임차 재임대 사업자 대상 세일즈 팁 (초기 실험) |
| 2021 | 18 | **4,590** | 0 | - | **FREE AirDNA 코스 1.0** 12편 → 채널 최고 평균 조회 |
| 2022 | 37 | 2,256 | 0 | - | 마스터클래스 2.0 (16편) + 세일즈 코스 (10편) + 시장 분석 리포트 판매 |
| 2023 | 18 | 1,350 | **87** | 1,037 | **쇼츠 전환** — 롱폼 절반으로 줄고 쇼츠 87편 투입 |
| 2024 | 38 | 1,431 | 44 | **1,975** | 라이브 워크숍·무료 코스 리뉴얼, 쇼츠 히트("This Airbnb Host gets it" 2.4만) |
| 2025 | 41 | 1,137 | 108 | 1,134 | 세금(STR Tax Loophole)·라이브 딜 분석·고객 사례 시리즈 |
| 2026 (9월까지) | 19 | 525 | 101 | 543 | "Making My Best Friend Rich" 에피소드 시리즈, 조회수 하락기 |

관찰:
- **조회수 정점은 2021년**. 무료 코스 12편이 채널 총조회의 7%(4.9만)를 만들었고, 이후 평균 조회는 매년 낮아진다.
- 2023년부터 **쇼츠 위주 볼륨 전략**으로 전환. 쇼츠가 편수의 66%, 조회수의 53%를 차지하지만 구독 전환·댓글은 롱폼이 압도적(댓글 있는 영상 비율 롱폼 88% vs 쇼츠 40%).
- 2026년은 롱폼·쇼츠 모두 평균 500회대로 **채널 피로 구간**. 최근 12개월 롱폼 24편의 최고 조회가 1,187회에 그친다.

---

## 3. 콘텐츠 포트폴리오

### 3-1. 롱폼 179편 카테고리 (제목 키워드 자동 분류)

| 카테고리 | 편수 | 평균조회 | 중앙값 | 합계조회 | 대표 콘텐츠 |
|----------|-----:|--------:|-------:|---------:|-------------|
| A. 무료 강의/코스 | 54 | 2,021 | 1,096 | 109,121 | FREE AirDNA Course 1.0 (12편), DATA MASTERCLASS 2.0 (16편), Airbnb Data To Make Sales (10편), Airbnb Data Basics, STR Tax Loophole Crash Course (4편) |
| C. 툴 튜토리얼/매물 분석 | 42 | 1,903 | 780 | 79,909 | AIRDNA Beginners Tutorial (2.5만), AIRDNA Tutorial 2025 (1.3만), STOP USING RENTALIZER, BNBcalc 2025, LIVE Airbnb Deal Analysis 시리즈 |
| D. 운영/리스팅 최적화 | 21 | 1,173 | 854 | 24,636 | Ultimate Airbnb Photography Guide (7.1천), Tier Ranking Firepits/Gamerooms, 어메니티 데이터 |
| G. 인사이트/투자 논평 | 18 | 2,712 | 608 | 48,814 | $1,000,000 AIRBNB CLEANING BUSINESS (3만, 채널 1위), 8 Game-Changing Lessons 2024, Airbnb Saturation |
| F. 사례/인터뷰/스토리 | 17 | 1,527 | 646 | 25,962 | $20,000/Month from 5 Airbnbs (7.3천), 고객 성공 사례, 전문가 대담 (AirDNA 수석 이코노미스트 등) |
| E. 세금/재무 | 13 | 821 | 627 | 10,668 | STR Tax Loophole, Big Beautiful Bill 100% 보너스 감가상각, 1031 교환 |
| B. 시장 선정/지역 | 10 | 761 | 764 | 7,613 | Flagstaff·Salt Lake·Louisville·Michigan·Poconos 시장 분석, 포화도 판별법 |
| H. 기타 | 4 | 1,012 | 1,092 | 4,049 | |

- **코스(A)와 툴 튜토리얼(C)이 롱폼 편수의 54%, 조회수의 61%**. 채널의 실질 엔진.
- 논평(G)은 평균이 높지만 중앙값이 가장 낮다 → 1편(청소 사업)의 아웃라이어 효과. 시장별 분석(B)은 지역이 좁아 조회가 가장 낮다.

### 3-2. 쇼츠 344편 유형

| 유형 | 편수 | 평균조회 | 합계조회 | 특징 |
|------|-----:|--------:|---------:|------|
| S4. 의견/소통/일상 | 194 | 1,035 | 200,789 | "This Airbnb Host gets it!!!!!", "I'm not a golfer." 같은 캡션형 제목. 남의 숙소 투어·리액션 |
| S1. 어메니티/디자인 | 74 | 1,316 | 97,362 | 온수욕조·파이어핏·게임룸·조명 등 "돈 되는 어메니티" 쇼케이스. **쇼츠 중 평균 최고** |
| S2. 수익/사례 숫자 | 51 | 723 | 36,851 | "Client just did $51K in One Month" 류 |
| S3. 데이터/분석 팁 | 25 | 884 | 22,103 | |

쇼츠 제목은 검색용이 아니라 인스타 릴스 캡션을 그대로 옮긴 형태(느낌표 다수, 문장형). 릴스·틱톡과 동시 배포하는 크로스포스팅 운영으로 보인다.

---

## 4. 시리즈(코스) 구조와 감쇠 데이터

| 시리즈 | 편수 | 1편 조회 | 마지막 편 조회 | 합계 | 잔존율 |
|--------|-----:|--------:|--------------:|-----:|-------:|
| FREE AirDNA Data Course 1.0 (2021.02) | 12 | 17,691 | 1,950 | 48,934 | 11% |
| DATA MASTERCLASS 2.0 (2022.04, 하루 16편 일괄 공개) | 16 | 7,652 | 952 | 35,302 | 12% |
| Airbnb Data To Make Sales (2022.10) | 10 | 1,429 | 398 | 5,757 | 28% |
| STR Tax Loophole Crash Course (2025.02) | 4 | 684 | 476 | 2,358 | 70% |

- 코스형 시리즈는 **1편 → 마지막 편 잔존율 약 10%**. 그래도 1편이 채널 유입 허브 역할을 하고, 시리즈 전체가 재생목록으로 묶여 "40시간 무료 코스"라는 신뢰 자산이 된다.
- 2024년 이후에는 긴 시리즈 대신 **단일 장편 코스**("Airbnb Data Basics | Everything You Need To Know" 3.7천, "Watch these 38 minutes if you want a cash flowing Airbnb" 5.8천)로 전환 → 감쇠 문제를 피하는 선택.
- "Watch these 38 minutes…"는 좋아요/조회 29.5%라는 비정상적 참여율 → 코스 수강 조건으로 좋아요를 유도한 것으로 추정.

---

## 5. 조회수 TOP 콘텐츠

### 롱폼 TOP 12

| 순위 | 제목 | 업로드 | 조회수 | 좋아요 |
|-----:|------|--------|-------:|-------:|
| 1 | $1,000,000 AIRBNB CLEANING BUSINESS! Absolute Must Watch for Airbnb Entrepreneurs | 2022-04 | 30,423 | 956 |
| 2 | AIRDNA (2021/2022) // BEGINNERS TUTORIAL By The Airbnb Data Guy! | 2021-09 | 25,373 | 516 |
| 3 | FREE!! AIRBNB / AIRDNA Data Course - Part 1 - AirDNA.co Overview/Tutorial | 2021-02 | 17,691 | - |
| 4 | AIRDNA Tutorial 2025: The ONLY Step by Step Guide You Need! | 2025-02 | 12,946 | 369 |
| 5 | AirDNA / Airbnb DATA MASTERCLASS 2.0 \| Part 1: Introduction to Everything | 2022-04 | 7,652 | 109 |
| 6 | $20,000/Month from 5 Airbnbs: Here's How He Did It | 2024-11 | 7,255 | 881 |
| 7 | The Ultimate Airbnb Photography Guide: Transform Your Listing in Just a Few Easy Steps | 2023-01 | 7,131 | 226 |
| 8 | My AirDNA 5 Step Process to $100,000 a Year Airbnbs | 2020-03 | 7,027 | 186 |
| 9 | Watch these 38 minutes if you want a cash flowing Airbnb | 2024-08 | 5,763 | 1,700 |
| 10 | FREE!! AIRBNB / AIRDNA Data Course - Part 2 - Airbnb Regulation | 2021-02 | 5,040 | - |
| 11 | FREE!! AIRBNB / AIRDNA Data Course - Part 4 - How You Extract Airbnb Data From AirDNA | 2021-02 | 4,877 | - |
| 12 | AirDNA / Airbnb DATA MASTERCLASS 2.0 \| Part 3: Avoiding Bad Data! | 2022-04 | 4,717 | 73 |

- TOP 12 중 **8편이 "AirDNA" 튜토리얼/코스**. 특정 툴 이름을 제목에 넣은 검색형 콘텐츠가 롱테일 조회를 만든다 (AirDNA는 제목 50편, 설명란 72편에 등장).
- 1위(청소 사업)는 채널 주제에서 벗어난 영상 → 주제 이탈 콘텐츠가 최고 조회를 내는 전형적 패턴이며, 구독 전환에는 기여하지 못한 것으로 보인다.

### 쇼츠 TOP 10

| 순위 | 제목 | 업로드 | 조회수 |
|-----:|------|--------|-------:|
| 1 | This Airbnb Host gets it!!!!! | 2024-07 | 23,905 |
| 2 | Joshua Tree Airbnb - CRUSHING IT!! | 2023-11 | 11,926 |
| 3 | I'm not a golfer. | 2024-05 | 10,608 |
| 4 | I'm extremely grateful | 2025-06 | 9,157 |
| 5 | Know the DATA behind amenities!!!!!!!!! | 2024-06 | 8,553 |
| 6 | How to MARKET a Hot Tub!!!!!! | 2024-10 | 5,560 |
| 7 | Again, I'm not the expert here. Just reporting the news! | 2025-06 | 4,939 |
| 8 | Genius marketing move by Andy! | 2024-06 | 4,934 |
| 9 | Still blows my mind how analyzing some data can lead to making a bunch of money! | 2025-05 | 3,870 |
| 10 | I understand that this is not a perfect analysis. | 2026-03 | 3,850 |

쇼츠 상위권은 대부분 **남의 독특한 숙소(골프 시뮬레이터, 조슈아트리 등)를 보여주며 수익 데이터를 덧붙이는 형식**. 본인 얼굴 강의형 쇼츠는 상위에 없다.

---

## 6. 성과 패턴 인사이트

| 항목 | 실측 | 해석 |
|------|------|------|
| 길이별 평균 조회 | 장편(30분+) 1,877 > 중편 1,733 > 단편 1,448 > 쇼츠 1,038 | 이 채널에선 **길수록 잘 본다**. 튜토리얼·코스 수요가 길이를 정당화 |
| 길이별 평균 좋아요 | 장편 91 > 중편 42 > 쇼츠 26 | 참여도 격차는 조회 격차보다 크다 |
| 롱폼 평균 길이 추이 | 2022년 19분 → 2024년 61분 → 2025~26년 29분 | 2024년 라이브 워크숍·2시간 분석 실험 후 30분대로 회귀 |
| 업로드 요일 (롱폼) | 화 42, 목 38, 토 26 | 화·목 고정 업로드 패턴 |
| 제목 공식 | "FREE" 34편, 달러 금액 17편, 연도 11편 | `FREE` + `AirDNA` + `$금액` + `연도` 조합. 최근작은 "He Spent $276K On This Airbnb... Here's How Much He Made" 류 사례형으로 이동 |
| 설명란 CTA | 롱폼 97%에 strsearch.com 링크 | 모든 롱폼이 서비스 랜딩페이지로 연결 |
| 참여율 상위 | "Watch these 38 minutes" 29.5%, "$20,000/Month from 5 Airbnbs" 12.1%, "8 Game-Changing Lessons" 10.4% | 좋아요 유도 장치 + 연말 결산형 콘텐츠가 참여를 만든다 |

---

## 7. 핵심 메시지 & 반복 프레임워크

채널 전체를 관통하는 주장은 3가지다.

1. **"감이 아니라 데이터로 산다"** — 초보 투자자가 "집을 먼저 고르고 나중에 수익을 계산"하는 역순을 비판. 2026년 시리즈 "How to Know If an Airbnb Will Actually Make Money"의 핵심 훅.
2. **20% 룰 / Airbnb판 1% 룰** — 연 매출이 매입가의 20% 이상 나와야 현금흐름이 가능하다는 한 줄 스크리닝. 시장 선정 2단계 = ① 규제 확인 → ② 20% 룰.
3. **어메니티는 데이터로 검증** — 온수욕조·파이어핏·게임룸을 "Tier Ranking"으로 매출 기여도별 서열화. 쇼츠 S1 유형(74편)이 이 메시지를 반복 노출.

형식 특징: AirDNA·스프레드시트 화면 공유 + 얼굴 캠, 20~40분 장편이 주력. 2025년 이후 "LIVE Airbnb Deal Analysis"(실제 매물 6개 중 1개만 합격) 같은 **실시간 판정형** 포맷 추가.

---

## 8. 수익 모델 & 퍼널

```
쇼츠 (숙소 투어 + 수익 숫자, 릴스/틱톡 크로스포스팅)      ← 도달
   → 롱폼 AirDNA 튜토리얼 / 무료 코스 40시간                 ← 검색 유입 + 신뢰
      → 설명란 strsearch.com 링크 (롱폼 97%)                 ← 전환
         → STR Search 유료 서비스
              ├ Air Valuation : 매물 발굴 대행 ("32일 안에 현금흐름 나는 Airbnb 매칭")
              ├ Air Optimization : 어메니티·타깃 고객 기반 리스팅 최적화
              └ Profit Map : 시장 분석 리포트
         → 고객 성공 사례 영상 ("STR Search Client Story")  ← 사회적 증거로 재투입
```

- 파트너·스폰서 노출: Techvestor(3편), Rentalizer(3편), HostShare(2편), BNBcalc, Stayamo, 세무 전문가(Brandon Hall·Ryan Bakke) 시리즈 → 세금 콘텐츠(13편)는 파트너 협업 성격.
- 팟캐스트 게스트 출연(REL Freedom, STR Riches, SmartStay Show, AirDNA STR Data Lab, REI Diamonds 등 10개 이상)으로 채널 외부 도달 확장. 모든 출연이 "The Airbnb Data Guy" 명칭으로 통일.

---

## 9. 강점 / 약점

**강점**
- 니치가 명확: "Airbnb × 데이터"를 6년 반 유지, 별명 자체가 검색 키워드
- 툴 이름(AirDNA) 튜토리얼이 롱테일 검색 유입을 지속 생성 (2021년 영상이 지금도 TOP 3)
- 무료 코스 분량(40시간+)이 경쟁 채널 대비 진입장벽
- 롱폼 설명란 97% CTA, 고객 사례 영상으로 퍼널이 닫혀 있음

**약점 / 리스크**
- 구독자 1.2만·총조회 67만은 6년 운영 대비 소규모. 유튜브는 브랜딩 채널이지 수익 채널이 아님
- **2026년 평균 조회 500회대로 하락** — 쇼츠 볼륨(월 10편+)이 롱폼 품질을 잠식
- 쇼츠 제목이 캡션형이라 유튜브 검색·추천에 불리 (릴스 크로스포스팅의 부작용)
- 미국 시장·AirDNA 툴 의존도가 높아 해외(한국) 시청자에게 직접 적용 어려움

---

## 10. 도이옥(한옥 스테이) 프로젝트 시사점

| 벤치마킹 포인트 (실측 근거) | 도이옥 적용안 |
|-----------------------------|---------------|
| 툴 튜토리얼이 TOP 12 중 8편 | 한국 호스트용 툴(에어비앤비 호스트 앱, 가격 설정, 채널 매니저) 튜토리얼을 검색형 롱폼으로 제작. 본 저장소의 **한옥 전수조사 스크래퍼·대시보드** 자체가 "툴" 콘텐츠가 됨 |
| 장편(30분+)이 평균 조회·좋아요 최고 | 짧은 쇼츠보다 "서울 한옥 스테이 전수조사 38분 완전판" 같은 장편 1편이 신뢰 자산 |
| 코스 시리즈 잔존율 ~10% | 12편 쪼개기보다 단일 장편 + 목차 타임스탬프 방식이 효율적 |
| 쇼츠 상위 = 남의 독특한 숙소 + 수익 숫자 | 북촌·서촌 한옥 스테이 투어 + "이 집 월 예약률 ○○%" 데이터 자막 쇼츠 (대시보드 데이터 활용) |
| 어메니티 Tier Ranking (S1 유형이 쇼츠 평균 최고) | 한옥 어메니티(마당·툇마루·온돌·다도·족욕)의 예약률·평점 상관을 수집 데이터로 서열화해 시리즈화 |
| 20% 룰 = 한 줄 스크리닝 | 한옥 스테이용 손익분기 공식 1개 만들기 (예: 월 예약률 × 객단가 ≥ 임대료+운영비 × 1.3) |
| 설명란 CTA 97% + 고객 사례 재투입 | 모든 영상 설명란에 도이옥 예약 링크·컨설팅 신청 링크 고정, 투숙객 후기·수익 사례를 영상으로 재활용 |
| 브랜드명 = 검색어, 전 플랫폼 동일 핸들 | "도이옥" 채널명·핸들을 유튜브/인스타/틱톡에 통일 (Notion "릴스해커" 기획과 동일 원칙) |
| 주제 이탈 1위 영상(청소 사업) | 한옥 리모델링·청소·운영비 같은 인접 주제도 한 번씩 실험할 가치 있음 |

---

## 11. 데이터 수집 방법 및 재현

```bash
pip install pandas openpyxl tabulate requests
python src/youtube_channel_analysis.py https://youtube.com/@theairbnbdataguy
```

- 기본 백엔드는 유튜브 내부 API(`youtubei.googleapis.com`)의 browse/next 엔드포인트로 영상·쇼츠·라이브 탭 전체를 순회하고 영상별 업로드일·조회수·좋아요·댓글수·길이·설명을 수집한다. 중간 저장 CSV로 재개 가능.
- 이번 수집 한계: 태그는 미수집(로그인 필요 엔드포인트), 쇼츠 길이는 미상, 댓글수는 댓글 0건이거나 비활성인 영상에서 빈값.
- 카테고리는 제목 키워드 규칙(`CATEGORY_RULES`, `SHORTS_RULES`)으로 자동 분류한 값이라 경계 사례에서 오분류가 있을 수 있다.

### 참고 자료
- 채널: https://www.youtube.com/@theairbnbdataguy
- STR Search: https://strsearch.com/ , https://johnbianchi.mykajabi.com/
- 팟캐스트·블로그 소개문: REL Freedom Podcast, Short Term Rental Riches #267, SmartStay Show, REI Diamonds, AirDNA STR Data Lab #96, Zen and the Art of Real Estate Investing #219
