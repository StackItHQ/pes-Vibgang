from google_sheets import get_sheet_data, update_sheet_data
from db_utils import insert_data_to_db, fetch_data_from_db

def sync_sheet_to_db():
    # Fetch data from Google Sheets
    sheet_data = get_sheet_data()

    # Skip the header row (assuming the first row is a header)
    if sheet_data:
        sheet_data = sheet_data[1:]

    # Insert the data into MySQL
    insert_data_to_db(sheet_data)
    print("Synced data from Google Sheets to MySQL!")

def sync_db_to_sheet():
    # Fetch data from MySQL
    db_data = fetch_data_from_db()

    # Format data for Google Sheets (assuming you want to include headers)
    formatted_data = [['ID', 'Name', 'Email', 'Age']] + db_data

    # Update Google Sheets with data from MySQL
    update_sheet_data(formatted_data)
    print("Synced data from MySQL to Google Sheets!")

if __name__ == '__main__':
    sync_sheet_to_db()  # Uncomment this line to sync from sheet to DB
    sync_db_to_sheet()  # Uncomment this line to sync from DB to sheet
