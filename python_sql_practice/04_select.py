import os
import sqlite3

# Define database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "databases", "favorites.db")

def select_examples():
    """
    Demonstrates standard SELECT operations using sqlite3:
    1. SELECT * (all columns)
    2. Selecting specific columns (language, problem)
    3. Retrieving rows using fetchall() and row indexing
    """
    print("Executing select_examples.py...")

    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Example 1: Selecting all columns (using LIMIT to avoid flooding the console)
        print("\n--- Example 1: SELECT * FROM favorites LIMIT 5 ---")
        cursor.execute("SELECT * FROM favorites LIMIT 5;")
        all_rows = cursor.fetchall()
        for row in all_rows:
            # columns: id, Timestamp, language, problem
            print(f"ID: {row[0]}, Time: {row[1]}, Language: {row[2]}, Problem: {row[3]}")

        # Example 2: Selecting specific columns
        print("\n--- Example 2: SELECT language, problem FROM favorites LIMIT 5 ---")
        cursor.execute("SELECT language, problem FROM favorites LIMIT 5;")
        specific_rows = cursor.fetchall()
        for row in specific_rows:
            # columns: language, problem
            print(f"Language Chosen: {row[0]}, Problem: {row[1]}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    select_examples()
