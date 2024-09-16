import time
from sync import sync_sheet_to_db, sync_db_to_sheet

POLL_INTERVAL = 30  # Interval in seconds

while True:
    sync_sheet_to_db()
    sync_db_to_sheet()
    time.sleep(POLL_INTERVAL)
