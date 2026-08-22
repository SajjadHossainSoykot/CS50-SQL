import os
import sqlite3

# Define database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "databases", "favorites.db")

def filtering_examples():
    """
    Demonstrates SQL filtering concepts using the WHERE clause:
    1. Direct value match: WHERE language = 'Python'
    2. LIKE operator with wildcards:
       - '%Scratch%' (matches anywhere)
       - 'Mario%' (matches beginning)
       - '%Readability' (matches end)
    """
    print("Executing filtering_examples.py...")

    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Example 1: Direct Value Match
        print("\n--- Example 1: SELECT * FROM favorites WHERE language = 'Python' LIMIT 3 ---")
        cursor.execute("SELECT id, language, problem FROM favorites WHERE language = ? LIMIT 3;", ("Python",))
        for row in cursor.fetchall():
            print(f"ID: {row[0]}, Language: {row[1]}, Problem: {row[2]}")

        # Example 2: LIKE with wildcard anywhere (%Scratch%)
        print("\n--- Example 2: WHERE problem LIKE '%Scratch%' LIMIT 3 ---")
        cursor.execute("SELECT id, language, problem FROM favorites WHERE problem LIKE ? LIMIT 3;", ("%Scratch%",))
        for row in cursor.fetchall():
            print(f"ID: {row[0]}, Language: {row[1]}, Problem: {row[2]}")

        # Example 3: LIKE with wildcard at end (Mario%)
        print("\n--- Example 3: WHERE problem LIKE 'Mario%' LIMIT 3 ---")
        cursor.execute("SELECT id, language, problem FROM favorites WHERE problem LIKE ? LIMIT 3;", ("Mario%",))
        for row in cursor.fetchall():
            print(f"ID: {row[0]}, Language: {row[1]}, Problem: {row[2]}")

        # Example 4: LIKE with wildcard at beginning (%Readability)
        print("\n--- Example 4: WHERE problem LIKE '%Readability' LIMIT 3 ---")
        cursor.execute("SELECT id, language, problem FROM favorites WHERE problem LIKE ? LIMIT 3;", ("%Readability",))
        for row in cursor.fetchall():
            print(f"ID: {row[0]}, Language: {row[1]}, Problem: {row[2]}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    filtering_examples()
