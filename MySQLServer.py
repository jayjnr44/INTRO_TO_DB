import mysql.connector

my_database = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="felixmania16",
    database="alx_book_store"  # Updated to match the new database name
)

try:
    my_cursor = my_database.cursor()
    try:
           my_cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
           print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
    finally:
        my_cursor.close()
        my_database.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")


