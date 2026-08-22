import os
import sqlite3

# Dynamically locate the databases directory relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "databases", "favorites.db")

def test_connection():
    """
    Demonstrates how to safely connect to a SQLite database, execute a simple
    connection test query, handle potential errors, and ensure the connection
    is closed properly in all scenarios.
    """
    print("Executing database_connection.py...")
    print(f"Connecting to: {DB_PATH}")

    conn = None
    try:
        # Establish connection to the database
        conn = sqlite3.connect(DB_PATH)
        print("Successfully connected to the database!")

        # Create a cursor object to execute queries
        cursor = conn.cursor()

        # Run a test query to verify SQLite version
        cursor.execute("SELECT sqlite_version();")
        
        # Fetch the query result
        version = cursor.fetchone()
        print(f"SQLite Library Version: {version[0]}")

    except sqlite3.Error as e:
        print(f"An error occurred while connecting to SQLite: {e}")

    finally:
        # Ensure the connection is always closed to release resources
        if conn:
            conn.close()
            print("Database connection closed successfully.")

if __name__ == "__main__":
    test_connection()
