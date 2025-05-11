import requests
import logging
from s3_uploader import upload_json_to_s3
import os


def fetch_exchange_rates():

    EXCHANGE_RATE_API_URL = os.getenv('EXCHANGE_URL')
    API_KEY = os.getenv('EXCAHNGE_API_KEY')

    params = {
        'authkey': API_KEY,
        'data': 'AP01'
    }
    try:
        response = requests.get(EXCHANGE_RATE_API_URL, params=params, verify=False)  # SSL 검증 비활성화
        response.raise_for_status()
        data = response.json()
        if data and data[0]['result'] == 1:
            return data
        else:
            logging.error("No exchange rate data available or invalid response")
            return None
    except requests.RequestException as e:
        logging.error(f"Error fetching exchange rates: {e}")
        raise Exception(e)

def process_exchange_rates(data):   
    return data

def upload_exchange_rates():

    print("환율 정보 업로드 중...")

    try:
        data = fetch_exchange_rates()
        if data:
            processed_data = process_exchange_rates(data)
            if upload_json_to_s3(processed_data, 'exchange_rates.json'):
                print("환율 정보가 S3에 성공적으로 업로드되었습니다.")
                return True
            else:
                print("환율 정보 데이터 S3 업로드 실패")
    except Exception as e:
        logging.error("환율 정보 데이터 S3 업로드 실패: %s", e)
        print("환율 정보 데이터 S3 업로드 실패")
        return False
    return False