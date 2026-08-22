import os
import sqlite3

# Define database paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAVORITES_DB = os.path.join(BASE_DIR, "..", "databases", "favorites.db")
SHOWS_DB = os.path.join(BASE_DIR, "..", "databases", "shows.db")

def grouping_examples():
    """
    Demonstrates SQL GROUP BY and HAVING clauses:
    1. Grouping favorites by language and getting counts.
    2. Grouping IMDb shows by genre, counting them, and using HAVING to filter groups.
    """
    print("Executing grouping_examples.py...")

    # 1. Grouping in favorites.db
    print("\n=== Grouping in favorites.db (Language Popularity) ===")
    conn_fav = sqlite3.connect(FAVORITES_DB)
    cursor_fav = conn_fav.cursor()

    cursor_fav.execute("""
        SELECT language, COUNT(*) AS count
        FROM favorites
        GROUP BY language
        ORDER BY count DESC;
    """)
    for row in cursor_fav.fetchall():
        print(f"Language: {row[0]:<10} Count: {row[1]}")

    conn_fav.close()

    # 2. Grouping in shows.db (Genres with count filter)
    print("\n=== Grouping in shows.db (Genres with HAVING clause) ===")
    conn_shows = sqlite3.connect(SHOWS_DB)
    cursor_shows = conn_shows.cursor()

    cursor_shows.execute("""
        SELECT genre, COUNT(*) AS count
        FROM genres
        GROUP BY genre
        HAVING count > 15000
        ORDER BY count DESC;
    """)
    for row in cursor_shows.fetchall():
        print(f"Genre: {row[0]:<15} Number of Shows: {row[1]:,}")

    conn_shows.close()

if __name__ == "__main__":
    grouping_examples()
