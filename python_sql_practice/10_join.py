import os
import sqlite3

# Define database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SHOWS_DB = os.path.join(BASE_DIR, "..", "databases", "shows.db")

def join_examples():
    """
    Demonstrates SQL JOIN queries (specifically INNER JOINs) to link relational tables:
    1. Simple Join: shows + ratings (combining show details and ratings)
    2. Multi-table Join: shows + genres + ratings (combining three tables)
    3. Many-to-many Join: shows + stars + people (finding actors for a specific show)
    """
    print("Executing join_examples.py...")

    conn = None
    try:
        conn = sqlite3.connect(SHOWS_DB)
        cursor = conn.cursor()

        # Example 1: Simple Join between shows and ratings
        print("\n--- Example 1: Join shows and ratings (Top 3 shows from 2020 by rating) ---")
        query_simple_join = """
        SELECT s.title, s.year, r.rating, r.votes
        FROM shows s
        INNER JOIN ratings r ON s.id = r.show_id
        WHERE s.year = 2020 AND r.votes > 10000
        ORDER BY r.rating DESC
        LIMIT 3;
        """
        cursor.execute(query_simple_join)
        for row in cursor.fetchall():
            print(f"- {row[0]} ({row[1]}) | Rating: {row[2]} | Votes: {row[3]:,}")

        # Example 2: Multi-table Join (shows + genres + ratings)
        print("\n--- Example 2: Three-table Join (Comedy shows from 2021 with ratings) ---")
        query_three_join = """
        SELECT s.title, g.genre, r.rating
        FROM shows s
        INNER JOIN genres g ON s.id = g.show_id
        INNER JOIN ratings r ON s.id = r.show_id
        WHERE s.year = 2021 AND g.genre = 'Comedy' AND r.votes > 5000
        ORDER BY r.rating DESC
        LIMIT 3;
        """
        cursor.execute(query_three_join)
        for row in cursor.fetchall():
            print(f"- {row[0]} | Genre: {row[1]} | Rating: {row[2]}")

        # Example 3: Many-to-many Join (shows + stars + people) to list cast members
        print("\n--- Example 3: Many-to-Many Join (Cast of 'Breaking Bad') ---")
        query_cast = """
        SELECT p.name
        FROM people p
        INNER JOIN stars st ON p.id = st.person_id
        INNER JOIN shows s ON st.show_id = s.id
        WHERE s.title = 'Breaking Bad' AND s.year = 2008;
        """
        cursor.execute(query_cast)
        for row in cursor.fetchall():
            print(f"- {row[0]}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    join_examples()
