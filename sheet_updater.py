import gspread
from google.oauth2.service_account import Credentials
from config import SCOPES, SERVICE_ACCOUNT_FILE, SHEET_URL

def get_sheet():
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(credentials)
    return client.open_by_url(SHEET_URL)

def format_data_for_sheet(data, fields):
    return [[row.get(field, "") for field in fields] for row in data]

def update_google_sheet(sheet, base_data, option_data, base_fields, option_fields):
    base_rows = format_data_for_sheet(base_data, base_fields)
    option_rows = format_data_for_sheet(option_data, option_fields)

    sheet.clear()
    sheet.append_row(base_fields)
    sheet.append_rows(base_rows)

    sheet.append_row([])
    sheet.append_row(["OptionList"])
    sheet.append_row(option_fields)
    sheet.append_rows(option_rows)