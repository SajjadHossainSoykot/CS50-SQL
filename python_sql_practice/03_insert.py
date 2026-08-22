import os
import sqlite3

# Define database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "databases", "favorites.db")

def insert_examples():
    """
    Demonstrates how to insert new records into a database using
    parameterized SQL queries (using ? placeholders) to safely prevent SQL injection.
    """
    print("Executing insert_examples.py...")

    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Ensure the table exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students_practice (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            track TEXT NOT NULL CHECK(track IN ('Scratch', 'C', 'Python', 'SQL', 'Web')),
            enrolled_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # 1. Insert a single record using parameterized queries (SQL injection safe)
        insert_single_query = """
        INSERT INTO students_practice (name, track)
        VALUES (?, ?);
        """
        cursor.execute(insert_single_query, ("Carter", "Python"))
        print("Inserted single record: Carter (Python)")

        # 2. Insert multiple records using cursor.executemany
        students_data = [
            ("Albert", "SQL"),
            ("Bobby", "C"),
            ("David", "Web"),
            ("Emma", "Scratch")
        ]
        cursor.executemany(insert_query := """
        INSERT INTO students_practice (name, track)
        VALUES (?, ?);
        """, students_data)
        print(f"Batch inserted {len(students_data)} records using executemany.")

        # Commit transactions to make changes persistent
        conn.commit()

        # Print the records to confirm insertion
        cursor.execute("SELECT id, name, track, enrolled_timestamp FROM students_practice;")
        rows = cursor.fetchall()
        print("\nCurrent records in 'students_practice':")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Track: {row[2]}, Enrolled: {row[3]}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    insert_examples()
