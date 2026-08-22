import os
import shutil
import sqlite3

# Define relative paths based on the directory containing this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORIGINAL_DB = os.path.join(BASE_DIR, "..", "databases", "favorites.db")
TEMP_DB = os.path.join(BASE_DIR, "..", "databases", "favorites_temp.db")

def main():
    print("Executing 11_delete_drop.py...")
    
    # 1. Create a temporary copy of the database to keep the original database completely safe
    print(f"Creating a temporary copy of the database at: {TEMP_DB}")
    if os.path.exists(TEMP_DB):
        os.remove(TEMP_DB)
    shutil.copyfile(ORIGINAL_DB, TEMP_DB)

    conn = None
    try:
        # Connect to the temporary database
        conn = sqlite3.connect(TEMP_DB)
        cursor = conn.cursor()

        # Let's verify what data exists first in the temporary database
        print("\n--- Step 1: Initial Count of Python submissions in favorites ---")
        cursor.execute("SELECT COUNT(*) FROM favorites WHERE language = 'Python';")
        before_delete = cursor.fetchone()[0]
        print(f"Submissions before delete: {before_delete}")

        # 2. Demonstrate DELETE operation
        # We delete all Python submissions from the 'favorites' table
        print("\n--- Step 2: Executing DELETE FROM favorites WHERE language = 'Python' ---")
        cursor.execute("DELETE FROM favorites WHERE language = 'Python';")
        conn.commit()

        # Check count again after delete
        cursor.execute("SELECT COUNT(*) FROM favorites WHERE language = 'Python';")
        after_delete = cursor.fetchone()[0]
        print(f"Submissions after delete:  {after_delete}")

        # 3. Demonstrate DROP TABLE operation
        # Check if table exists (it should, as we just ran queries on it)
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='favorites';")
        table_exists_before = cursor.fetchone()
        print(f"\n--- Step 3: Verifying 'favorites' table existence ---")
        print(f"Table exists? {table_exists_before is not None}")

        # Execute DROP TABLE
        print("Executing DROP TABLE favorites...")
        cursor.execute("DROP TABLE favorites;")
        conn.commit()

        # Check again if table exists after drop
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='favorites';")
        table_exists_after = cursor.fetchone()
        print(f"Table exists after DROP? {table_exists_after is not None}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("\nTemporary database connection closed.")
        
        # 4. Clean up the temporary database copy so it does not persist in the repository
        if os.path.exists(TEMP_DB):
            os.remove(TEMP_DB)
            print("Successfully deleted the temporary database file. Original database remains completely untouched.")

if __name__ == "__main__":
    main()
