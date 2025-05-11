import FinanceDataReader as fdr
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging
from s3_uploader import upload_json_to_s3

def get_commodity_prices(commodities, periods):
    try:
        end_date = datetime.now()
        all_data = {commodity: {} for commodity in commodities}
        
        index = 0
        keys = list(commodities.keys())

        for period in periods:
            if period.endswith('d'):
                days = int(period[:-1])
                start_date = end_date - timedelta(days=days)
                freq = 'D'
            elif period.endswith('m'):
                months = int(period[:-1])
                start_date = end_date - pd.DateOffset(months=months)
                freq = 'W' if months <= 6 else 'M'
            elif period.endswith('y'):
                years = int(period[:-1])
                start_date = end_date - pd.DateOffset(years=years)
                freq = 'M' if years <= 5 else 'Q'
            else:
                raise ValueError("Invalid period format. Use 'd' for days, 'm' for months, 'y' for years.")
            
            for name, symbol in commodities.items():
                df = fdr.DataReader(symbol, start_date, end_date)
                resampled = df['Close'].resample(freq).last()
                valid_data = resampled.dropna()
                
                all_data[name][period] = [{
                    "date": date.strftime('%Y-%m-%d'),
                    "price": float(price)
                } for date, price in valid_data.items() if not np.isnan(price)]

            print(f"Successfully fetched data : {keys[index]}")       
            index += 1
            
        
        return all_data
    except Exception as e:
        logging.error(f"Error in get_commodity_prices: {str(e)}")
        return None

def all_get_commodity_prices():
    commodities = {
        'Gold': 'GC=F',       # COMEX 금 선물
        'Silver': 'SI=F',     # COMEX 은 선물
        'Crude Oil': 'CL=F',  # WTI 원유 선물
        'Copper': 'HG=F',     # COMEX 구리 선물
        'Platinum': 'PL=F',   # NYMEX 백금 선물
        'Natural Gas': 'NG=F',# 천연 가스 선물
        'Corn': 'ZC=F',       # 옥수수 선물
        'Wheat': 'ZW=F'       # 밀 선물
    }

    periods = ['5d', '30d', '6m', '1y', '5y', '20y']
    
    try:
        all_data = get_commodity_prices(commodities, periods)
        if all_data is not None:
            print("Successfully fetched data for all periods and commodities")
            return all_data
        else:
            print("Failed to fetch data")
            return None
    except Exception as e:
        logging.error(f"Error in all_get_commodity_prices: {str(e)}")
        print(f"An error occurred. Check the log file for details.")
        return None

def upload_metal_info():
    print("금속 시세 정보 업로드중")
    try:
        # 데이터 수집
        result = all_get_commodity_prices()

        if result is not None:
            # S3에 JSON으로 업로드
            json_success = upload_json_to_s3(result, 'all_metal_prices.json')
        
            if json_success: 
                print("금속 시세 정보가 S3에 성공적으로 업로드되었습니다.")
                return True
            else:
                print("금속 시세 정보 데이터 S3 업로드 실패")
                return False
        else:
            print("데이터 수집 실패")
            return False
    except Exception as e:
        logging.error("금속 시세 정보 데이터 S3 업로드 실패: %s", e)
        print("금속 시세 정보 데이터 S3 업로드 실패")
        return False