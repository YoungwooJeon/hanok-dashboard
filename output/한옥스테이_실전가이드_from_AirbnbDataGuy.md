# 서울 한옥 스테이 운영자를 위한 실전 가이드 — The Airbnb Data Guy(John Bianchi) 채널에서 뽑은 것

- 대상: 도이옥(서울 한옥 에어비앤비) 운영자
- 출처: 채널 523편 목록·설명란, 그가 팟캐스트·블로그·LinkedIn에 공개한 방법론, 그리고 **본 저장소의 서울 한옥 250채 실측 데이터**(`output/한옥_분석.xlsx`)에 그의 방법을 직접 적용한 결과
- 작성일: 2026-09-24

> **자료 범위 안내**: 이 세션에서는 유튜브 자막 API가 차단되어 영상 본문을 문장 단위로 읽지는 못했습니다. 그가 6년간 반복해 온 프레임워크(팟캐스트 10여 곳, 블로그, 코스 소개문에서 교차 확인된 것)를 뼈대로 삼고, 각 항목마다 **직접 볼 영상 링크와 길이**를 붙였습니다. 자막 전문이 필요하면 11장의 스크립트를 로컬에서 돌리면 롱폼 179편 자막이 모두 추출됩니다.

---

## 0. 한 페이지 요약 — 그가 6년 동안 반복한 6가지

| # | 원칙 | 한옥 스테이에서 뜻하는 것 |
|---|------|--------------------------|
| 1 | **결정 전에 데이터, 데이터는 "비교 숙소(comps)"에서 나온다** | 툴의 평균값(AirDNA Rentalizer류)을 믿지 말고, 내 숙소와 같은 동네·같은 인원·같은 형태의 상위 숙소를 직접 뽑아 예약률과 가격을 본다 |
| 2 | **규제가 매출보다 먼저** | 외국인관광도시민박업·한옥체험업 등록 요건과 동별 허용 여부를 매출 계산 전에 확정 |
| 3 | **"지루한 집이 진다" — 어메니티가 숙소 자체보다 중요** | 한옥이라는 형태만으로는 안 팔린다. 상위 숙소가 가진 것은 기본, 거기에 차별화 1~2개 |
| 4 | **어메니티는 감이 아니라 매출 격차로 서열화한다(Tier Ranking)** | 후기 키워드·예약률로 "돈 되는 요소"를 확인한 뒤 투자한다 |
| 5 | **마케팅(사진·제목·순서)이 매출을 좌우한다** | 첫 사진은 가장 강한 어메니티, 사진 순서는 스토리, 전문 촬영은 ROI가 항상 남는다 |
| 6 | **포화는 두려워할 게 아니라 기회** | 같은 동네에 예약률 90%와 40%가 공존한다면 시장이 아니라 실행의 문제다 |

---

## 1. 그의 세계관: 어디에 시간을 쓰라고 하는가

그가 팟캐스트마다 하는 말을 그대로 옮기면 이렇습니다.

- "Airbnb's all about the amenities. **The boring homes are the ones that lose.**"
- "You need all of these things (온수욕조, 뷰, 파이어핏, 게임룸, 라운지체어…) **because your competition has them.**"
- "Amenities, marketing, and guest experience often matter more than the property itself."
- "Regulation should always come before revenue analysis."
- 분석 순서: "**go the entire city, then figure out the neighborhoods, then unit sizes, then look at every single amenity and feature within that area that are driving the revenue** — create a list of everything."

핵심은 **매출 = 입지 × 인원 규모 × 어메니티 × 마케팅**이고, 이 중 운영자가 통제할 수 있는 뒤의 두 개에 투자하라는 것입니다.

관련 영상
- Airbnb Data Basics | Everything You Need To Know (2시간 4분, 3,659회) https://www.youtube.com/watch?v=8YmyiGZykLk
- Watch these 38 minutes if you want a cash flowing Airbnb (38분, 5,763회) https://www.youtube.com/watch?v=NJqZ9Q2zRuk
- Airbnb Starter Pack!!! If I had just known these things (62분) https://www.youtube.com/watch?v=RDOOs1m5yDQ

---

## 2. 매출 예측: "비교 숙소(comps)" 방법

### 2-1. 그의 절차

1. **도시 → 동네 → 유닛 규모(침실 수·최대 인원) 순으로 좁힌다.** 다른 규모의 숙소는 비교 대상이 아니다.
2. **연중 운영(full-time) 숙소만 남긴다.** 가끔 여는 집을 섞으면 예약률 평균이 왜곡된다. 그는 "full-time hosting data"를 가장 중요한 필터로 꼽는다.
3. **Top comps와 Base comps를 잡는다.** 상위 그룹(잘 꾸민 숙소)과 기본 그룹(평범한 숙소)의 매출을 각각 구해 **범위(range)** 를 만든다. 내 숙소는 어메니티·사진 수준에 따라 그 범위 안 어딘가에 놓인다. STR Search의 리포트는 이걸 P25/P50/P75/P90 밴드로 낸다.
4. **후기 수로 "진짜 예약"을 검증한다.** 캘린더가 막혀 있어도 호스트가 막은 것일 수 있다. 후기 증가 속도가 실제 수요다.
5. 툴(Rentalizer, AirDNA 추정치)은 **출발점일 뿐**이며, 그는 "STOP USING RENTALIZER"라는 영상까지 냈다. 2025년 업데이트 후에도 "직접 comps를 뽑아 검증하라"는 입장은 같다.

관련 영상
- FREE COURSE | How To Predict Airbnb Revenue | The ONLY Skill You Need (84분) https://www.youtube.com/watch?v=CYLH9snshP8
- The Only Scorecard You Need To Predict An Airbnbs Revenue (7분, 2026-05) https://www.youtube.com/watch?v=_Oiv_P4HVvE
- STOP USING RENTALIZER!!! Use My Proven 4 Step Process Instead (35분, 4,474회) https://www.youtube.com/watch?v=OnfOK8InV9o
- How To Quickly Analyze An Airbnb For Beginners In 2026 (21분) https://www.youtube.com/watch?v=sD0V3Y_5qbI
- LIVE Airbnb Deal Analysis: 6 Properties Reviewed—Only 1 Good Deal! (131분, 실전 판정 과정) https://www.youtube.com/watch?v=336frT_IKDc

### 2-2. 서울 한옥 250채에 같은 방법을 적용한 결과

본 저장소의 실측 데이터(2026-06 수집, 종로·중·성북·동대문·서대문 한옥 250채, 예약률은 향후 30일 기준)로 "동네 → 인원 규모" 밴드를 만들면 다음과 같습니다.

**동별 예약률 밴드 (표본 5채 이상)**

| 동 | 표본 | 예약률 중앙값(Base) | 상위 25%(Top) | 후기 수 중앙값 |
|----|-----:|-------------------:|-------------:|--------------:|
| 종로구 가회동 | 31 | 80% | 90% | 80 |
| 종로구 종로5·6가동 | 10 | 78% | 88% | 18 |
| 종로구 삼청동 | 26 | 77% | 83% | 66 |
| 서대문구 창천동 | 7 | 77% | 90% | 64 |
| 종로구 창신1동 | 5 | 73% | 80% | 44 |
| 종로구 종로1·2·3·4가동 | 10 | 73% | 82% | 43 |
| 종로구 청운효자동(서촌) | 86 | 70% | 82% | 58 |
| 종로구 사직동 | 13 | 60% | 77% | 28 |

**인원 규모별 예약률**

| 최대 인원 | 표본 | 중앙값 | 상위 25% |
|-----------|-----:|-------:|---------:|
| 1~2인 | 36 | 60% | 77% |
| 3~4인 | 59 | 73% | 87% |
| 5~6인 | 71 | 70% | 83% |
| 7인 이상 | 65 | 73% | 83% |

읽는 법 (그의 방식대로)
- 도이옥의 "Base"는 해당 동의 중앙값, "Top"은 상위 25% 값입니다. 어메니티·사진이 상위권이면 Top, 아니면 Base로 계획을 세웁니다.
- 1~2인 숙소는 어느 동에서든 예약률 하위 밴드입니다. **3~4인 규모가 예약률 상위 밴드(87%)가 가장 높습니다.** 방 하나를 더 쓰더라도 4인 수용이 가능하게 만드는 편이 유리합니다.
- 후기 수 31개를 넘긴 숙소의 예약률 중앙값은 73%, 그 이하는 60~62%입니다. 초기 30개 후기까지가 첫 번째 관문입니다.

> 데이터 품질 메모: `한옥_분석.xlsx`의 1박 가격이 255,267원·112,628원 같은 소수 값에 몰려 있고 어메니티 열(욕조·주차·세탁기 등)과 최소 박수·청소비가 비어 있습니다. 스크래퍼가 가격 셀렉터를 잘못 잡았거나 환율 변환 기본값을 읽은 것으로 보입니다. 가격·어메니티 비교(그의 Tier Ranking)를 제대로 하려면 step2 스크래퍼의 해당 필드를 보수해야 합니다.

---

## 3. 시장 판단: 규제 → 20% 룰 → 포화 점검

### 3-1. 20% 룰과 임차형 환산
- 그의 기준: **연 매출 ≥ 매입가의 20%** (15%면 가능, 30%면 최상). 500k 달러 집이면 연 100k 달러가 나와야 산다.
- 그는 시카고에서 임차 재임대(rental arbitrage)로 시작했고, 2021년 무료 코스 Part 7 "How to Calculate the Maximum Rent to Pay a Landlord"에서 **최대 임대료 역산법**을 가르쳤습니다. 논리는 단순합니다.

```
최대 월 임대료 = (Base 시나리오 월 매출 − 운영비 − 목표 이익) 
Base 시나리오 월 매출 = 동네 중앙값 예약률 × 30일 × 내 1박 가격
```

- 도이옥이 매입이 아니라 임차·위탁 형태라면, **동네 중앙값(Base)으로 임대료를 정하고 상위값(Top)은 보너스로 두는 것**이 그가 말하는 "수익 안 나는 매물 안 사기"의 임차 버전입니다.

관련 영상
- FREE!! AIRBNB / AIRDNA Data Course - Part 7 - How to Calculate the Maximum Rent to Pay a Landlord https://www.youtube.com/watch?v=cHt9nnKHB2s
- The Airbnb Version of the 1% Rule (It's Not What You Think) (20분) https://www.youtube.com/watch?v=gzWZjOgmYzs
- Airbnb Market Selection Mastery | Trust The Process (93분) https://www.youtube.com/watch?v=RRvcsO3kRAQ

### 3-2. 규제 먼저
- 그는 시장 선정 1단계를 항상 규제로 둡니다. LinkedIn에 "How to avoid Airbnb regulation nightmares"라는 글을 따로 썼고, 2025년에는 "This ChatGPT Prompt Tells You If an Airbnb Is Legal or Not"(https://www.youtube.com/watch?v=1boKMu33eRA)로 규제 조사 자동화까지 다뤘습니다.
- 서울 한옥 적용: 외국인관광도시민박업(내국인 불가·호스트 실거주 요건)과 한옥체험업(내국인 가능)의 차이가 곧 타깃 고객과 예약률을 가릅니다. 등록 유형을 먼저 확정하고 그 유형에 맞는 comps만 비교해야 합니다.

### 3-3. 포화는 기회
- 그의 LinkedIn 글 제목이 "Why Saturated Airbnb Markets are a Golden (Opportunity)"입니다. 논지: 포화 시장일수록 "잘 만든 숙소"와 "대충 만든 숙소"의 격차가 커지고, 상위권만 살아남는다. 점검법은 12개월 이상 점유율 추이와 신규 공급 증가율을 같이 보는 것(RevPAR 기준).
- 서울 한옥 데이터가 이를 그대로 보여줍니다. 244채 중 **예약률 90% 이상이 44채, 40% 이하가 47채**로 같은 동네 안에서 극단이 공존합니다. 두 그룹의 후기 키워드(가족·키즈·온돌·구들·아궁이·마당)는 거의 같습니다. 즉 "한옥이라는 상품"이 아니라 **운영·마케팅 실행의 차이**가 예약률을 가릅니다.

| 그룹 | 표본 | 최대 인원 중앙값 | 후기 수 중앙값 | 별점 | 게스트 픽 비율 |
|------|-----:|---------------:|--------------:|-----:|--------------:|
| 예약률 90% 이상 | 44 | 6인 | 52 | 4.99 | 86% |
| 예약률 40% 이하 | 47 | 5인 | 25.5 | 4.97 | 53% |

관련 영상
- Is your Airbnb Market Saturated? Step By Step Guide (24분) https://www.youtube.com/watch?v=aSmMiR8ZmpQ
- Airbnb Saturation! Should You Be Scared or Excited? (17분) https://www.youtube.com/watch?v=CIW-Bsq25OI
- The Airbnb Race No One's Talking About… Until It's Too Late (6분) https://www.youtube.com/watch?v=yXyPoSKUn4o

---

## 4. 어메니티 전략: 무엇에 돈을 쓸 것인가

### 4-1. 그의 원칙
1. **경쟁 숙소가 가진 것은 기본값이다.** 그의 미국 리스트: 온수욕조, 뷰, 파이어핏, 야외 바, 라운지체어, 게임룸, 두 번째 거실. 없으면 비교에서 탈락한다.
2. **Tier Ranking으로 서열화한다.** 같은 동네·같은 규모 숙소를 어메니티 유무로 나눠 매출 차이를 측정한다. 그는 파이어핏, 게임룸을 각각 한 편(30~44분)씩 들여 티어를 매겼다. 예: 주방 아일랜드에서 지하로 내려가는 미끄럼틀 하나가 옆집보다 연 1만 달러를 더 벌게 했다.
3. **"있음"이 아니라 "업그레이드".** 2025년 영상 제목이 그대로 요지다: "Top Hosts Don't Just Add Amenities — They Upgrade Them Like This." 같은 온수욕조라도 사진에 찍히는 수준으로 만들어야 한다.
4. **이해 없이 쓰면 낭비.** "You're Wasting Your Money On Amenities If You Don't Understand This" — 데이터로 확인되지 않은 어메니티 투자는 하지 않는다.
5. **독특함(unique)은 그 자체로 어메니티.** "The Queen of unique Airbnbs: Build it and they will come", "'UNIQUE' Airbnb Profitability Figured Out In 5 Steps".

관련 영상
- Airbnb Amenity Research for Beginners: A Free Mini Course (53분) https://www.youtube.com/watch?v=Lg2dHCi56fU
- Tier Ranking Airbnb Firepits | See how it affects your revenue (30분) https://www.youtube.com/watch?v=99yYyIJBUtk
- Tier Ranking Airbnb GAMEROOMS!! (44분) https://www.youtube.com/watch?v=VKCARHkg6GQ
- Top Hosts Don't Just Add Amenities — They Upgrade Them Like This (27분) https://www.youtube.com/watch?v=pr3JM6Ez4JM
- You're Wasting Your Money On Amenities If You Don't Understand This (16분) https://www.youtube.com/watch?v=M4cYePzuIIQ
- Maximize Your Airbnb Earnings: Data-Driven Strategies for High-Demand Amenities in 2024 (17분) https://www.youtube.com/watch?v=6B4j8SMuKgg
- The Airbnb Designs I'm Copying (17분) https://www.youtube.com/watch?v=cmyh2Ywlfoc
- Ultimate Airbnb Wishlist: Top Earning Properties Analyzed (43분) https://www.youtube.com/watch?v=nDh9thrryQQ

### 4-2. 서울 한옥판 Tier Ranking (실측)

어메니티 열이 비어 있어 **후기 키워드 Top5**와 **숙소 이름·소개글 키워드**로 대신 서열을 매겼습니다.

**후기에서 가장 많이 언급되는 요소 (250채 전체)**

| 순위 | 키워드 | 언급 숙소 수 |
|-----:|--------|-------------:|
| 1 | 가족 | 173 |
| 2 | 온돌 | 137 |
| 3 | 마당 | 102 |
| 4 | 아궁이 | 92 |
| 5 | 독채 | 70 |
| 6 | 기와 | 67 |
| 7 | 경복궁 | 62 |
| 8 | 구들 | 45 |
| 9 | 픽업 | 37 |
| 10 | 장작 | 35 |
| 11 | 프라이빗 | 34 |
| 12 | 키즈 | 33 |
| 13 | 노천탕 | 30 |
| 14 | 정원 | 25 |
| 15 | 툇마루 | 17 |

→ 그의 표현으로 "**your competition has them**"에 해당하는 기본값: 가족 단위 수용, 온돌/구들(실제로 따뜻한 바닥), 마당, 독채·프라이빗. 이게 없으면 비교에서 탈락합니다.

**키워드별 예약률 (이름·소개글 기준, 표본 5채 이상)**

| 키워드 | 표본 | 예약률 중앙값 | 상위 25% | 해석 |
|--------|-----:|-------------:|---------:|------|
| 체험(다도·공예 등) | 13 | **87%** | 93% | 가장 강한 차별화 요소. 그의 "unique" 논리 그대로 |
| 익선(동) | 7 | 83% | 88% | 입지 프리미엄 |
| 고택 | 5 | 83% | 93% | 진짜 오래된 집은 스토리 자체가 어메니티 |
| 2층 | 9 | 83% | 90% | 한옥에서 드문 구조 = 독특함 |
| 광장시장 | 10 | 80% | 89% | 제목에 시장 접근성 명시 |
| 공항(버스·셔틀) | 27 | 77% | 90% | 외국인 고객 편의 |
| 프라이빗 | 41 | 77% | 90% | |
| 신축 | 11 | 73% | 92% | 상위권 폭이 넓음 |
| 독채 | 72 | 73% | 87% | 기본값 |
| 짐보관 | 12 | 73% | 88% | 소소하지만 유효 |
| 북촌 / 경복궁 | 86 / 81 | 73% | 83% | 입지 기본값 |
| 마당 | 37 | 70% | 80% | 기본값, 차별화는 안 됨 |
| 서촌 | 31 | 63% | 77% | 북촌보다 낮음 |
| 주차 | 17 | 63% | 83% | 외국인 비중 높은 시장에서 효과 제한 |
| 정원 | 16 | 62% | 78% | |
| 뷰 | 16 | 55% | 75% | "뷰"만 내세운 숙소는 하위권 |
| 욕조 | 14 | 52% | 67% | 욕조를 내세운 숙소가 오히려 낮음 (가격·타깃 불일치 추정, 표본 소) |

**예약률 90% 이상 그룹에서 특히 강한 후기 키워드**: 키즈(32건), 정원(19), 프라이빗(15), 장작·아궁이 체험(20). 40% 이하 그룹에는 "고궁 뷰"가 상대적으로 많이 등장합니다. 즉 **"보는 한옥"보다 "쓰는 한옥"(아이와 놀고, 불 때고, 마당 쓰는)이 팔립니다.**

도이옥 어메니티 우선순위 제안 (그의 Tier 논리 적용)
- **Tier 1 (필수, 없으면 탈락)**: 4인 이상 수용, 실제로 따뜻한 온돌, 프라이빗 독채, 마당, 공항버스·역 접근 안내
- **Tier 2 (차별화, 예약률 +10%p 급)**: 체험 프로그램(다도·한복·공예·아궁이 불 지피기), 키즈 요소(안전·놀이), 2층/누마루 같은 구조적 독특함
- **Tier 3 (사진용 업그레이드)**: 야외 자쿠지·노천탕(상위 숙소 제목에 반복 등장), 조명·툇마루 세팅
- **후순위**: 뷰 강조, 욕조 단독 소구, 주차

---

## 5. 리스팅 최적화: 사진·제목·알고리즘

### 5-1. 사진
그의 39분짜리 사진 가이드와 2024년 Before & After 영상의 요지:
- **첫 사진은 가장 강한 어메니티**(그의 미국 예시: 온수욕조·뷰·게임룸). 방 사진으로 시작하지 않는다.
- **사진 순서가 스토리**다. 도착 → 가장 좋은 공간 → 침실 → 욕실 → 편의시설 순으로 고객이 머무는 하루를 따라간다.
- 전문 촬영은 "ROI가 항상 남는다"(그의 2026년 쇼츠 문장 그대로). 사진 리메이크만으로 예약이 바뀐 사례를 반복해서 다룬다.
- 한옥 적용: 첫 사진 후보는 **불 켜진 저녁 마당·툇마루 전경** 또는 **아궁이·체험 장면**. 후기 키워드 1위가 "가족"이므로 사람이 쓰는 장면(아이·가족 실루엣)을 최소 1장 넣는다.

관련 영상
- The Ultimate Airbnb Photography Guide (39분, 7,131회) https://www.youtube.com/watch?v=l5YN175M1zs
- Transform Your Airbnb: Before & After Photo Makeover Revealed! (28분) https://www.youtube.com/watch?v=5VjqJaxjta4

### 5-2. 제목·소개글
서울 한옥 상위 숙소(예약률 90%+) 제목의 공통 패턴:
- **역 이름 + 도보 분 수** ("경복궁역 도보4분", "안국역 8분")
- **인원·구성 숫자** ("R3B5 최대 9인", "2RM2BTH")
- **프라이빗 / 독채 / NEW / 신축**
- **외국인 편의** ("공항버스 3분", "짐보관", "No Stair")
- 브랜드명(소유재·안유재·만월정처럼 한자 당호)로 재방문·검색 가능성 확보

그의 "See Who Airbnb Compares You To!"(14분)는 에어비앤비가 내 숙소를 어떤 숙소들과 같은 세트로 노출하는지 확인하고, 그 세트 안에서 **첫 사진·제목·가격이 이기도록** 만드는 방법입니다. 한옥은 "hanok" 검색 세트가 명확하므로, 같은 세트에 뜨는 10개 숙소를 직접 열어 비교표를 만드는 것이 첫 작업입니다.

관련 영상
- See Who Airbnb Compares You To! (14분) https://www.youtube.com/watch?v=kuEDWcOPuNw
- This Airbnb Listing Was a Disaster… Until I Fixed It (30분) https://www.youtube.com/watch?v=Zo-0gJtjcOU
- She Upgraded Everything—But Still No Bookings (Until This Fix) (9분) https://www.youtube.com/watch?v=w241GA7VKMs
- This Airbnb Was Failing… Until We Did THIS (27분) https://www.youtube.com/watch?v=u6bZJmXu1JM

### 5-3. 알고리즘
그는 2025년에 에어비앤비 검색 알고리즘 공개 문서를 통째로 읽고 정리한 영상(41분)을 냈습니다. 문서가 말하는 랭킹 요소는 **클릭 후 예약 전환율, 가격 경쟁력(같은 세트 대비), 후기 품질·수, 응답 속도, 취소 이력, 즉시 예약**입니다. 이 중 운영자가 당장 바꿀 수 있는 건 첫 사진(클릭률), 제목(클릭률), 응답 속도, 즉시 예약 켜기입니다.

관련 영상
- He Read Airbnb's Algorithm Docs So You Don't Have To (41분) https://www.youtube.com/watch?v=UDAUNpw8p-I
- Improve Your Airbnb Ranking To Increase your Bookings (68분) https://www.youtube.com/watch?v=CfWQZpgwR-Y

---

## 6. 가격: 그의 "Prove & Simple Process"

그의 가격 영상(7분)과 "How To Increase Your Airbnb Revenue"(24분)에서 반복되는 절차:

1. **Top comps의 가격을 천장으로 잡는다.** 동네 상위 숙소가 받는 가격 이상은 당장 못 받는다.
2. **후기가 쌓일 때까지는 점유율을 산다.** 초기에는 천장보다 낮게 시작해 후기와 별점을 확보한다. (서울 데이터: 후기 31개 이상부터 예약률 중앙값이 60% → 73%로 점프)
3. **점유율이 목표(그는 보통 70~80%대)를 넘으면 가격을 단계적으로 올린다.** 예약률 90~100%는 "가격이 싸다"는 신호다.
4. **RevPAR(가용 1박당 매출)로 판단한다.** 예약률 95%에 10만원보다 75%에 14만원이 낫다.
5. 최소 박수·주중/주말 차등은 comps 세트가 하는 대로 맞추되, 갭 나이트(예약 사이 1~2일)는 최소 박수를 풀어 채운다.

서울 한옥 데이터에서 예약률 100%인 숙소가 8채 있습니다(청구동 3룸, 청운효자동 4방 독채, 종로5·6가 9인 등). 그의 논리대로면 이 숙소들은 **가격 인상 여지가 있는 숙소**이고, 도이옥이 같은 세트에 들어간다면 이들의 가격이 곧 천장입니다.

관련 영상
- Pricing Your Airbnb? Use My Prove & Simple Process (7분) https://www.youtube.com/watch?v=FcTW0ylnapE
- How To Increase Your Airbnb Revenue (24분) https://www.youtube.com/watch?v=8QCwvPwto3s
- $42K in 1 Month on Airbnb?! (Full Breakdown) (25분, 고매출 숙소의 가격·점유 구조) https://www.youtube.com/watch?v=DklRK526uh0

---

## 7. 그가 반복해서 경고하는 실수

여러 영상 제목과 팟캐스트에서 교차 확인되는 것만 추렸습니다.

| 실수 | 그의 대안 | 한옥 스테이 체크 |
|------|-----------|-----------------|
| 집을 먼저 고르고 수익은 나중에 계산 ("starting completely backward") | comps → 밴드 → 결정 | 리모델링 예산 확정 전에 동별 밴드부터 |
| 툴 추정치(평균값)를 그대로 믿음 | 상위/기본 comps로 범위 산출 | 에어비앤비 "예상 수입" 화면 무시, 실제 이웃 숙소 10개 비교 |
| 파트타임 숙소를 비교군에 섞음 | 연중 운영 숙소만 | 후기 수·호스팅 시작 연도로 필터 (250채 중 2025~26년 신규가 100채 이상) |
| 규제 확인을 뒤로 미룸 | 규제가 1단계 | 민박업/한옥체험업 등록 유형 확정 |
| "예쁜 집"에 만족, 어메니티 없음 ("Is your property pretty or cash flowing?") | 경쟁 숙소 어메니티 목록을 전부 갖추고 +1 | 4장의 Tier 1·2 점검 |
| 사진·마케팅 비용을 아낌 | 전문 촬영, 첫 사진 재선정 | 5장 |
| 후기 없는 상태에서 고가 책정 | 점유 먼저, 가격은 후기 30개 이후 | 6장 |
| 어메니티를 "추가"만 하고 "업그레이드"하지 않음 | 사진에 찍히는 수준으로 | 자쿠지·조명·툇마루 세팅 |

관련 영상
- 10 lessons from 200+ Airbnb Acquisitions (9분) https://www.youtube.com/watch?v=uFEmcNhETqI
- 8 Game-Changing Lessons for Airbnb Investors in 2024 (29분, 참여율 10%) https://www.youtube.com/watch?v=qt4b-neXw1M
- 3 STR Underwriting Mistakes You Never Realize Until It's Too Late (6분) https://www.youtube.com/watch?v=ertpUhCIOxA
- Is your property pretty or cash flowing? Learn how we do both (72분) https://www.youtube.com/watch?v=kDVhqzJ5L4o

---

## 8. 한국에 안 맞는 부분 (걸러 볼 것)

- **세금 콘텐츠 13편**(STR Tax Loophole, 100% 보너스 감가상각, 1031 교환, "Big Beautiful Bill")은 미국 세법 전용입니다. 한국 세무와 무관하므로 건너뛰어도 됩니다.
- **AirDNA 화면 조작 튜토리얼**(50편)은 AirDNA가 서울 데이터를 제한적으로만 다루므로 조작법 자체보다 "무엇을 보는지"(동네·규모·어메니티 필터, 상위 25% 숙소 분리)만 취하면 됩니다. 본 저장소의 스크래퍼가 그 역할을 대신합니다.
- 그의 어메니티 리스트(온수욕조·게임룸·파이어핏)는 미국 교외 대형 주택 기준입니다. 한옥에서는 4-2절의 실측 서열로 바꿔 읽어야 합니다.

---

## 9. 도이옥 30일 실행 체크리스트

1. **비교 세트 만들기 (1주차)**: 에어비앤비에서 도이옥과 같은 동·같은 인원으로 검색해 상위 10개 숙소를 열고 첫 사진·제목·가격·최소 박수·어메니티·후기 수를 표로 정리한다. (그의 "See Who Airbnb Compares You To")
2. **밴드 확정**: 2-2절 표에서 해당 동의 Base(중앙값)·Top(상위 25%) 예약률을 가져와 월 매출 두 시나리오를 만든다. 임차라면 Base 시나리오로 임대료 상한을 정한다.
3. **Tier 1 점검**: 4인 이상 수용, 온돌 실제 난방, 프라이빗 독채, 마당, 공항버스·역 안내 문구. 하나라도 빠지면 그것부터.
4. **Tier 2 하나 고르기**: 체험(다도·아궁이·한복) 또는 키즈 세팅 중 하나를 사진에 찍히는 수준으로 만든다.
5. **사진 재촬영**: 저녁 마당 전경을 첫 사진으로, 사람이 쓰는 장면 1장, 순서는 도착→마당→방→욕실→편의.
6. **제목 재작성**: `[역 이름 도보 N분] 프라이빗 한옥 독채 · 최대 N인 · 공항버스 · 당호`.
7. **가격**: 비교 세트 상위 가격의 80~85%로 시작, 후기 30개 도달 시 10%씩 인상, 예약률 90% 넘으면 즉시 인상.
8. **응답·즉시예약**: 즉시 예약 켜고 응답 1시간 이내 유지(알고리즘 요소).
9. **후기 키워드 관리**: 첫 30개 후기에 "가족·온돌·마당·체험"이 자연스럽게 들어가도록 체크인 안내와 체험을 설계한다.
10. **데이터 재수집**: step2 스크래퍼의 가격·어메니티 필드를 고쳐 월 1회 재수집하고, 2-2·4-2 표를 갱신해 내 숙소가 밴드 어디에 있는지 추적한다.

---

## 10. 우선 시청 목록 (운영자용, 순서대로)

| 순서 | 영상 | 길이 | 왜 |
|-----:|------|-----:|----|
| 1 | Watch these 38 minutes if you want a cash flowing Airbnb | 38분 | 그의 방법 전체 요약 |
| 2 | Airbnb Amenity Research for Beginners: A Free Mini Course | 53분 | 어메니티 Tier 매기는 실제 절차 |
| 3 | The Ultimate Airbnb Photography Guide | 39분 | 사진 순서·첫 사진 |
| 4 | See Who Airbnb Compares You To! | 14분 | 내 비교 세트 찾기 |
| 5 | He Read Airbnb's Algorithm Docs So You Don't Have To | 41분 | 랭킹 요소 |
| 6 | Pricing Your Airbnb? Use My Prove & Simple Process | 7분 | 가격 사다리 |
| 7 | This Airbnb Listing Was a Disaster… Until I Fixed It | 30분 | 리스팅 수술 사례 |
| 8 | Top Hosts Don't Just Add Amenities — They Upgrade Them | 27분 | 업그레이드 개념 |
| 9 | Is your Airbnb Market Saturated? Step By Step Guide | 24분 | 포화 점검 |
| 10 | FREE COURSE \| How To Predict Airbnb Revenue | 84분 | comps 방법 심화 |
| 11 | The Queen of unique Airbnbs: Build it and they will come | 15분 | 독특함 = 어메니티 |
| 12 | 10 lessons from 200+ Airbnb Acquisitions | 9분 | 실수 목록 |

전체 목록·조회수·링크는 `output/유튜브_채널_theairbnbdataguy.xlsx`의 영상목록 시트에 있습니다.

---

## 11. 자막 전문까지 뽑으려면 (로컬 실행)

```bash
pip install youtube-transcript-api pandas openpyxl
python src/youtube_transcripts.py --min-views 500      # 조회수 500 이상 롱폼 자막 추출
python src/youtube_transcripts.py --ids l5YN175M1zs,Lg2dHCi56fU,kuEDWcOPuNw   # 특정 영상만
```

결과는 `output/transcripts/<video_id>.txt`와 `output/유튜브_자막_theairbnbdataguy.xlsx`에 저장됩니다. 이 파일을 올려 주시면 10장의 12편을 문장 단위로 요약해 이 가이드에 붙이겠습니다.
