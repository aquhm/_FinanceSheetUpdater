import boto3
import logging
import json
import pandas as pd
from io import StringIO, BytesIO
from config import S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION

def upload_to_s3(data, file_name, content_type):
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            region_name=AWS_REGION
        )

        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=file_name,
            Body=data,
            ContentType=content_type
        )

        print(f"{file_name} 파일이 S3에 업로드되었습니다.")
        return True

    except Exception as e:
        logging.error(f"S3 업로드 요청 실패: {e}")
        print("error:", e)
        return False

def upload_json_to_s3(data, file_name):
    json_data = json.dumps(data, ensure_ascii=False)
    return upload_to_s3(json_data.encode('utf-8'), file_name, 'application/json')

def upload_csv_to_s3(data, file_name):
    # JSON 데이터 구조 확인
    if isinstance(data, dict) and 'base_list' in data and 'option_list' in data:
        # base_list와 option_list를 별도의 DataFrame으로 변환
        base_df = pd.DataFrame(data['base_list'])
        option_df = pd.DataFrame(data['option_list'])
        
        # 두 DataFrame을 하나의 CSV 파일로 저장
        csv_buffer = StringIO()
        base_df.to_csv(csv_buffer, index=False)
        csv_buffer.write("\n\nOption List:\n")
        option_df.to_csv(csv_buffer, index=False)
    elif isinstance(data, list):
        # 데이터가 리스트 형태라면 직접 DataFrame으로 변환
        df = pd.DataFrame(data)
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
    else:
        # 다른 형태의 데이터에 대한 처리
        raise ValueError("Unsupported data structure for CSV conversion")
    
    return upload_to_s3(csv_buffer.getvalue(), file_name, 'text/csv')

def upload_data_to_s3(data, base_file_name):
    json_success = upload_json_to_s3(data, f"{base_file_name}.json")
    csv_success = upload_csv_to_s3(data, f"{base_file_name}.csv")
    return json_success and csv_success