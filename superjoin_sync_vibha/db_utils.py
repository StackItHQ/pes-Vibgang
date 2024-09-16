import mysql.connector
from mysql.connector import Error

def get_mysql_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='your-password', #leave it blank if not set password
        database='Students'
    )

def insert_data_to_db(data):
    connection = get_mysql_connection()
    cursor = connection.cursor()
    
    # Adjust your SQL query to handle CRUD operations
    insert_query = """
    INSERT INTO candidates (ID, Name, Email, Age) 
    VALUES (%s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE Name=VALUES(Name), Email=VALUES(Email), Age=VALUES(Age);
    """
    
    for row in data:
        cursor.execute(insert_query, (row[0], row[1], row[2], row[3]))
    
    connection.commit()
    cursor.close()
    connection.close()

def fetch_data_from_db():
    connection = get_mysql_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT ID, Name, Email, Age FROM candidates")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows
