import os
import sqlite3

# Define database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SHOWS_DB = os.path.join(BASE_DIR, "..", "databases", "shows.db")

def subquery_examples():
    """
    Demonstrates SQL subqueries (nested SELECT statements):
    1. Finding shows with ratings higher than the overall average rating.
    2. Finding shows associated with a specific writer ('Vince Gilligan') using ID nesting.
    """
    print("Executing subquery_examples.py...")

    conn = None
    try:
        conn = sqlite3.connect(SHOWS_DB)
        cursor = conn.cursor()

        # Example 1: Show titles with rating higher than the average rating of all shows
        print("\n--- Example 1: Shows rated above the global average rating ---")
        query_avg = """
        SELECT title, year FROM shows
        WHERE id IN (
            SELECT show_id FROM ratings
            WHERE rating > (SELECT AVG(rating) FROM ratings)
        )
        ORDER BY year DESC
        LIMIT 5;
        """
        cursor.execute(query_avg)
        for row in cursor.fetchall():
            print(f"- {row[0]} ({row[1]})")

        # Example 2: Shows written by Vince Gilligan using nested SELECTs
        print("\n--- Example 2: Shows written by 'Vince Gilligan' using subqueries ---")
        query_writer = """
        SELECT title, year FROM shows
        WHERE id IN (
            SELECT show_id FROM writers
            WHERE person_id = (
                SELECT id FROM people
                WHERE name = 'Vince Gilligan'
            )
        )
        ORDER BY year ASC;
        """
        cursor.execute(query_writer)
        for row in cursor.fetchall():
            print(f"- {row[0]} ({row[1]})")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    subquery_examples()
