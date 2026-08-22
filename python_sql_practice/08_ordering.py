import os
import sqlite3

# Define database paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAVORITES_DB = os.path.join(BASE_DIR, "..", "databases", "favorites.db")
SHOWS_DB = os.path.join(BASE_DIR, "..", "databases", "shows.db")

def ordering_examples():
    """
    Demonstrates SQL sorting and limits using ORDER BY and LIMIT:
    1. ORDER BY (sorting fields alphabetically)
    2. ORDER BY DESC (sorting counts/numeric fields in descending order)
    3. LIMIT (constraining the number of output rows)
    """
    print("Executing ordering_examples.py...")

    # 1. Ordering in favorites.db
    print("\n=== Ordering in favorites.db (Alphabetical Sorting) ===")
    conn_fav = sqlite3.connect(FAVORITES_DB)
    cursor_fav = conn_fav.cursor()

    cursor_fav.execute("""
        SELECT DISTINCT problem
        FROM favorites
        ORDER BY problem ASC
        LIMIT 5;
    """)
    print("First 5 problems (A-Z):")
    for row in cursor_fav.fetchall():
        print(f"- {row[0]}")

    conn_fav.close()

    # 2. Ordering in shows.db (Numeric Sorting)
    print("\n=== Ordering in shows.db (Highest Rated Shows by Votes) ===")
    conn_shows = sqlite3.connect(SHOWS_DB)
    cursor_shows = conn_shows.cursor()

    # Find the top 5 most highly voted shows with a rating of 9.0 or above
    cursor_shows.execute("""
        SELECT s.title, s.year, r.rating, r.votes
        FROM shows s
        JOIN ratings r ON s.id = r.show_id
        WHERE r.rating >= 9.0
        ORDER BY r.votes DESC
        LIMIT 5;
    """)
    print("Top 5 highly-voted shows (Rating >= 9.0):")
    for row in cursor_shows.fetchall():
        print(f"- {row[0]} ({row[1]}) | Rating: {row[2]} | Votes: {row[3]:,}")

    conn_shows.close()

if __name__ == "__main__":
    ordering_examples()
