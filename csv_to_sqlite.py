import csv
import os
import sqlite3

# Define relative paths based on the directory containing this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "favorites.csv")
DB_PATH = os.path.join(BASE_DIR, "databases", "favorites.db")

def main():
    print("CSV to SQLite Conversion Script")
    print(f"Source CSV: {CSV_PATH}")
    print(f"Target DB:  {DB_PATH}\n")

    # 1. Reset target database to start clean
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("Removed existing database to start fresh.")

    # 2. Connect to the SQLite database
    # sqlite3.connect will automatically create the file if it doesn't exist
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 3. Create the table schema
    # id is set as INTEGER PRIMARY KEY AUTOINCREMENT so SQLite automatically generates it.
    create_table_query = """
    CREATE TABLE favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Timestamp TEXT,
        language TEXT,
        problem TEXT
    );
    """
    cursor.execute(create_table_query)
    print("Created 'favorites' table with schema (id, Timestamp, language, problem).")

    # 4. Open the CSV file and read rows
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"Source CSV not found at: {CSV_PATH}")

    with open(CSV_PATH, "r", encoding="utf-8") as file:
        # csv.DictReader parses the first row of CSV as dictionary keys
        reader = csv.DictReader(file)
        
        # Prepare the INSERT query
        insert_query = """
        INSERT INTO favorites (Timestamp, language, problem)
        VALUES (?, ?, ?);
        """
        
        # Collect rows to perform a fast batch insert (executemany)
        rows_to_insert = []
        for row in reader:
            rows_to_insert.append((
                row["Timestamp"],
                row["language"],
                row["problem"]
            ))

        # 5. Insert all rows inside a transaction (executemany is highly optimized)
        cursor.executemany(insert_query, rows_to_insert)
        
    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print(f"Successfully imported {len(rows_to_insert)} rows into '{DB_PATH}'!")

if __name__ == "__main__":
    main()
