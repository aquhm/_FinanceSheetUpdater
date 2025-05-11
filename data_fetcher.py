import requests
import logging
from config import AUTH_KEY
from constants import FinancialSector

def fetch_financial_data(api_url, sector_code, page_number):
    params = {"auth": AUTH_KEY, "topFinGrpNo": sector_code, "pageNo": page_number}
    response = requests.get(api_url, params=params)

    try:
        response_json = response.json()
        result = response_json.get("result", None)

        if result is None or result["err_cd"] != "000":
            logging.error(f"API 요청 실패: {response.text}")
            return None

        return {
            "base_list": result.get("baseList", []),
            "option_list": result.get("optionList", []),
            "max_page_no": int(result["max_page_no"]),
            "now_page_no": int(result["now_page_no"]),
        }
    except Exception as e:
        logging.error(f"예외 발생: {e}")
        return None

def collect_all_data(api_url):
    all_data = {
        "base_list": [],
        "option_list": []
    }

    for sector in FinancialSector:
        page_no = 1
        while True:
            data = fetch_financial_data(api_url, sector.value, page_no)

            if not data:
                break

            all_data["base_list"].extend(data["base_list"])
            all_data["option_list"].extend(data["option_list"])

            if data["now_page_no"] >= data["max_page_no"]:
                break

            page_no += 1

    return all_data

def get_json_data(api_url):
    return collect_all_data(api_url)