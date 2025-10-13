import os
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

class GoogleSheetsUploader:
    def __init__(self, spreadsheet_name, worksheet_name, creds_path=None):
        self.creds_path = creds_path or os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON")
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
        credentials = Credentials.from_service_account_file(self.creds_path, scopes=scopes)
        self.client = gspread.authorize(credentials)
        self.spreadsheet = self.client.open(spreadsheet_name)
        self.worksheet = self.spreadsheet.worksheet(worksheet_name)

    def upload_dataframe(self, df: pd.DataFrame):
        self.worksheet.clear()
        self.worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        print(f"Datos subidos correctamente a Google Sheets: {self.worksheet.title}")
