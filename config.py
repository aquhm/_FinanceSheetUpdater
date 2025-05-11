import os
from dotenv import load_dotenv

load_dotenv()

AUTH_KEY = os.getenv('AUTH_KEY')
SHEET_URL = os.getenv('SHEET_URL')
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')

BASE_URL = "http://finlife.fss.or.kr/finlifeapi/"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

API_URLS = {
    "company": (f"{BASE_URL}companySearch.json", "회사 정보"),
    "deposit": (f"{BASE_URL}depositProductsSearch.json", "정기예금"),
    "saving": (f"{BASE_URL}savingProductsSearch.json", "정기적금"),
    "annuity": (f"{BASE_URL}annuitySavingProductsSearch.json", "연금저축"),
    "mortgage": (f"{BASE_URL}mortgageLoanProductsSearch.json", "주택담보대출"),
    "rent": (f"{BASE_URL}rentHouseLoanProductsSearch.json", "전세자금대출"),
    "credit": (f"{BASE_URL}creditLoanProductsSearch.json", "개인신용대출"),
}

# S3 설정
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'ap-northeast-2')