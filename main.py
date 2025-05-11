import logging
from config import API_URLS
from constants import API_FIELDS
from data_fetcher import get_json_data
from sheet_updater import get_sheet, update_google_sheet
from s3_uploader import upload_data_to_s3
from exchange_rate import upload_exchange_rates
from metal_price import upload_metal_info


logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def update_sheet():
    try:
        sh = get_sheet()
    except Exception as e:
        logging.error("Google Sheets 연결 에러: %s", e)
        return

    for api_name, (api_url, sheet_name) in API_URLS.items():
        print(f"{sheet_name} 데이터 수집 중...")
        json_data = get_json_data(api_url)

        print(f"{sheet_name} 데이터 시트에 업데이트 중...")
        sheet = sh.worksheet(sheet_name)
        update_google_sheet(sheet, json_data["base_list"], json_data["option_list"], 
                            API_FIELDS[api_name]["base"], API_FIELDS[api_name]["option"])

        print(f"{sheet_name} 데이터가 시트에 업데이트되었습니다.")

        # S3에 JSON 데이터 업로드
        if upload_data_to_s3(json_data, api_name):
            print(f"{api_name} 데이터가 S3에 JSON과 CSV 형식으로 업로드되었습니다.")
        else:
            print(f"{api_name} 데이터 S3 업로드 실패")

def main():
    
    # 금융 정보 업로드
    update_sheet()
    
    # 환율 정보 업로드    
    upload_exchange_rates()        

    # 금속 시세 정보 업로드    
    upload_metal_info()

    print("모든 데이터의 시트 업데이트 및 S3 업로드가 완료되었습니다.")

if __name__ == "__main__":
    main()