# 금융 데이터 수집 및 저장 시스템

금융감독원의 금융상품 API, 환율 정보, 금속 시세 등 다양한 금융 데이터를 수집하여 Google Sheets와 AWS S3에 자동으로 저장하는 파이썬 기반 시스템입니다.

## 📋 주요 기능

- **금융상품 정보 수집**: 금융감독원 오픈 API를 활용한 다양한 금융상품 정보 수집
  - 예금, 적금, 연금저축, 주택담보대출, 전세자금대출, 개인신용대출 등
  - 금융회사별 상품 정보 및 금리 데이터
- **환율 정보 수집**: 최신 환율 정보 API를 통한 데이터 수집

- **금속 시세 정보 수집**: FinanceDataReader를 활용한 다양한 원자재 시세 정보 수집

  - 금, 은, 원유, 구리, 백금, 천연가스, 옥수수, 밀 등
  - 다양한 기간별 데이터 (5일, 30일, 6개월, 1년, 5년, 20년)

- **데이터 저장 및 관리**:
  - Google Sheets 자동 업데이트
  - AWS S3 버킷에 JSON 및 CSV 형식으로 저장

## 🛠️ 기술 스택

- **Python 3.x**
- **데이터 수집 및 처리**:
  - Requests: HTTP 요청 처리
  - Pandas: 데이터 처리 및 분석
  - FinanceDataReader: 금융 데이터 수집
  - NumPy: 수치 연산
- **데이터 저장**:

  - gspread: Google Sheets API 연동
  - boto3: AWS S3 연동

- **구성 및 환경**:
  - python-dotenv: 환경 변수 관리
  - google-auth: Google API 인증

## ⚙️ 설치 방법

1. 저장소 클론

   ```bash
   git clone [저장소 URL]
   cd [프로젝트 폴더명]
   ```

2. 필요한 패키지 설치

   ```bash
   pip install -r requirements.txt
   ```

3. 환경 변수 및 서비스 계정 설정

   **환경 변수 설정하기**

   ```bash
   # .env.example 파일을 .env로 복사
   cp .env.example .env
   ```

   .env 파일을 열고 다음 정보를 입력하세요:

   ```
   # 인증 관련 설정
   AUTH_KEY=<금융감독원 API 인증 키를 입력하세요>

   # 구글 시트 관련 설정
   SHEET_URL=<사용할 구글 시트의 전체 URL을 입력하세요 (예: https://docs.google.com/spreadsheets/d/1AbCdEfGhIjKlMnOpQrStUvWxYz/edit#gid=0)>
   SERVICE_ACCOUNT_FILE=<구글 서비스 계정 JSON 파일의 경로를 입력하세요 (예: ./service_account.json)>

   # AWS S3 접근 정보
   S3_BUCKET_NAME=<사용할 S3 버킷 이름을 입력하세요>
   AWS_ACCESS_KEY_ID=<AWS IAM 콘솔에서 발급받은 액세스 키 ID를 입력하세요>
   AWS_SECRET_ACCESS_KEY=<AWS IAM 콘솔에서 발급받은 비밀 액세스 키를 입력하세요>
   AWS_REGION=ap-northeast-2

   # 환율 API 접근 정보
   EXCHANGE_URL=<환율 정보를 가져올 API URL을 입력하세요 (예: https://www.koreaexim.go.kr/site/program/financial/exchangeJSON/)>
   EXCAHNGE_API_KEY=<환율 API 사용을 위한 API 키를 입력하세요>
   ```

   **Google 서비스 계정 설정**

   ```bash
   # service_account_example.json 파일을 service_account.json으로 복사
   cp service_account_example.json service_account.json
   ```

   service_account.json 파일을 열고 Google Cloud Platform에서 발급받은 서비스 계정 정보를 입력하세요:

   ```json
   {
     "type": "service_account",
     "project_id": "<Google Cloud 프로젝트 ID를 입력하세요>",
     "private_key_id": "<서비스 계정의 private key ID를 입력하세요>",
     "private_key": "<서비스 계정의 private key를 입력하세요 (-----BEGIN PRIVATE KEY----- 로 시작하는 긴 문자열)>",
     "client_email": "<서비스 계정 이메일 주소를 입력하세요 (예: project-name@project-id.iam.gserviceaccount.com)>",
     "client_id": "<서비스 계정의 클라이언트 ID를 입력하세요>",
     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
     "token_uri": "https://oauth2.googleapis.com/token",
     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
     "client_x509_cert_url": "<서비스 계정의 x509 인증서 URL을 입력하세요>",
     "universe_domain": "googleapis.com"
   }
   ```

4. Google 서비스 계정 접근 권한 설정
   - service_account.json 파일의 `client_email` 값을 복사
   - 구글 스프레드시트에 해당 이메일 주소를 편집자로 공유

## 📊 사용 방법

1. 기본 실행 (모든 데이터 수집 및 저장)

   ```bash
   python main.py
   ```

2. 각 모듈별 개별 실행

   ```python
   # 환율 정보만 수집 및 저장
   from exchange_rate import upload_exchange_rates
   upload_exchange_rates()

   # 금속 시세 정보만 수집 및 저장
   from metal_price import upload_metal_info
   upload_metal_info()
   ```

## 🔄 워크플로우

1. **환경 설정**:

   - 환경 변수(.env) 및 서비스 계정(service_account.json) 파일 설정
   - API 키 및 인증 정보 확인

2. **데이터 수집**:

   - 금융감독원 API에서 금융 상품 정보 수집
   - 환율 API에서 최신 환율 정보 조회
   - FinanceDataReader를 통해 금속/원자재 시세 정보 가져오기

3. **데이터 처리**:

   - 수집된 데이터 정리 및 구조화
   - 필요한 계산 및 변환 수행

4. **데이터 저장**:

   - Google Sheets에 정보 업데이트
   - AWS S3 버킷에 JSON 및 CSV 형식으로 저장

5. **자동화** (선택적):
   - 스케줄러를 통한 주기적 데이터 수집 및 업데이트
   - 데이터 변화 모니터링

## 📁 프로젝트 구조

```
금융데이터수집시스템/
├── config.py           # 환경 설정 및 API 구성
├── constants.py        # 상수 정의 (금융 섹터, API 필드 등)
├── data_fetcher.py     # 금융 데이터 수집
├── exchange_rate.py    # 환율 정보 수집
├── main.py             # 메인 실행 파일
├── metal_price.py      # 금속 가격 정보 수집
├── s3_uploader.py      # AWS S3에 데이터 업로드
├── sheet_updater.py    # Google Sheets에 데이터 업데이트
├── .env.example        # 환경 변수 예시 파일
├── service_account_example.json  # 구글 서비스 계정 예시 파일
└── requirements.txt    # 필요한 라이브러리 목록
```

## 📊 데이터 수집 대상

### 금융상품 종류

- 정기예금 (deposit)
- 정기적금 (saving)
- 연금저축 (annuity)
- 주택담보대출 (mortgage)
- 전세자금대출 (rent)
- 개인신용대출 (credit)
- 금융회사 정보 (company)

### 금융권역 분류

- 은행 (BANK)
- 특수금융 (SPECIALIZED_FINANCIAL)
- 저축은행 (SAVINGS_BANK)
- 보험 (INSURANCE)
- 투자 (INVESTMENT)

### 금속/원자재 시세

- 금 (Gold)
- 은 (Silver)
- 원유 (Crude Oil)
- 구리 (Copper)
- 백금 (Platinum)
- 천연가스 (Natural Gas)
- 옥수수 (Corn)
- 밀 (Wheat)

## ⚠️ 주의사항

- 금융감독원 API는 인증키가 필요하며, 일일 사용량 제한이 있을 수 있습니다.
- AWS S3 사용 시 요금이 발생할 수 있습니다.
- 환경 변수 설정 파일(.env) 및 서비스 계정 파일(service_account.json)은 절대 저장소에 포함하지 마세요.
- API 키는 주기적으로 변경하는 것이 보안에 좋습니다.
- 권한 설정:
  - AWS IAM 사용자에게는 필요한 최소한의 권한만 부여하세요.
  - 구글 서비스 계정도 필요한 최소한의 권한만 부여하세요.

## 📝 라이선스

이 프로젝트는 MIT 라이선스에 따라 배포됩니다.
