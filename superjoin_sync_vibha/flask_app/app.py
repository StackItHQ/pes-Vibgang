import sys
import os
from flask import Flask, request, jsonify
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from google_sheets import get_sheet_data, update_sheet_data
from db_utils import insert_data_to_db, fetch_data_from_db

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask Google Sheets Sync API!"

@app.route('/update_sheet', methods=['POST'])
def update_sheet():
    data = request.json  # Assumes data is sent as JSON
    if 'values' not in data:
        return jsonify({"error": "Invalid data format"}), 400
    # Update Google Sheets with the received data
    update_sheet_data(data['values'])
    return jsonify({"status": "success"})

@app.route('/sync_sheet_to_db', methods=['POST'])
def sync_sheet_to_db():
    # Fetch data from Google Sheets
    data = get_sheet_data()
    # Skip the header row (assuming the first row is a header)
    data = data[1:]
    # Insert the data into MySQL
    insert_data_to_db(data)
    return jsonify({"status": "success"})

@app.route('/sync_db_to_sheet', methods=['POST'])
def sync_db_to_sheet():
    # Fetch data from MySQL
    db_data = fetch_data_from_db()
    # Format data for Google Sheets (assuming you want to include headers)
    formatted_data = [['ID', 'Name', 'Email', 'Age']] + db_data
    # Update Google Sheets with data from MySQL
    update_sheet_data(formatted_data)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

