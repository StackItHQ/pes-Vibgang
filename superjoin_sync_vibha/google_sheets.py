from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from db_utils import insert_data_to_db, fetch_data_from_db  # Import your new functions


# Set the scope of the API we want to interact with
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Replace with your Google Sheet ID
SHEET_ID = '1jzrUZr3PbOESxem7xWM1P4YU_L9D8Ly20WOQfnkTnTc'

# Authenticate using the credentials.json file
def authenticate_google_sheets():
    creds = Credentials.from_service_account_file('/Users/vibhagangolli/Desktop/google-sheets-sync/credentials.json', scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    return service.spreadsheets()

# Function to read data from the Google Sheet
def get_sheet_data(sheet_range='Sheet1!A1:D'):
    service = authenticate_google_sheets()
    result = service.values().get(spreadsheetId=SHEET_ID, range=sheet_range).execute()
    rows = result.get('values', [])
    return rows

# Function to write data to the Google Sheet
def update_sheet_data(values, sheet_range='Sheet1!A1:D10'):
    service = authenticate_google_sheets()
    body = {
        'values': values
    }
    service.values().update(
        spreadsheetId=SHEET_ID,
        range=sheet_range,
        body=body,
        valueInputOption='RAW'
    ).execute()

# Sync from Google Sheets to MySQL
def sync_sheet_to_db():
    sheet_data = get_sheet_data()
    # Skip the header row
    sheet_data = sheet_data[1:]
    # Insert or update data in MySQL
    insert_data_to_db(sheet_data)
    print("Synced data from Google Sheets to MySQL!")

# Sync from MySQL to Google Sheets
def sync_db_to_sheet():
    db_data = fetch_data_from_db()
    # Format data for Google Sheets (including headers)
    formatted_data = [['ID', 'Name', 'Email', 'Age']] + db_data
    update_sheet_data(formatted_data)
    print("Synced data from MySQL to Google Sheets!")

# Example usage
if __name__ == '__main__':
    sync_sheet_to_db()  # Uncomment to sync from Sheets to DB
    sync_db_to_sheet()  # Uncomment to sync from DB to Sheets
