import os
import sqlite3

# Define database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "databases", "favorites.db")

def create_tables():
    """
    Demonstrates how to define a table schema programmatically using
    SQL constraints (PRIMARY KEY, AUTOINCREMENT, NOT NULL, DEFAULT).
    Using CREATE TABLE IF NOT EXISTS keeps this script repeatable and safe.
    """
    print("Executing create_tables.py...")
    
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Define schema for a sample 'students_practice' table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS students_practice (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            track TEXT NOT NULL CHECK(track IN ('Scratch', 'C', 'Python', 'SQL', 'Web')),
            enrolled_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        # Execute create statement
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'students_practice' verified/created successfully.")

        # Show the table schema
        cursor.execute("PRAGMA table_info(students_practice);")
        columns = cursor.fetchall()
        print("\nColumns in 'students_practice' table:")
        for col in columns:
            print(f"- Name: {col[1]}, Type: {col[2]}, NotNull: {bool(col[3])}, Default: {col[4]}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    create_tables()
