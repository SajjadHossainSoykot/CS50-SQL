import os
import sqlite3

# Define database paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FAVORITES_DB = os.path.join(BASE_DIR, "..", "databases", "favorites.db")
SHOWS_DB = os.path.join(BASE_DIR, "..", "databases", "shows.db")

def aggregation_examples():
    """
    Demonstrates SQL Aggregation functions:
    1. COUNT(*) - count all records
    2. COUNT(DISTINCT column) - count unique entries
    3. AVG(), MIN(), MAX() - statistical aggregations on numeric columns in ratings (shows.db)
    """
    print("Executing aggregation_examples.py...")

    # 1. Aggregations on favorites.db
    print("\n=== Aggregations on favorites.db ===")
    conn_fav = sqlite3.connect(FAVORITES_DB)
    cursor_fav = conn_fav.cursor()

    # Count total entries
    cursor_fav.execute("SELECT COUNT(*) FROM favorites;")
    total_count = cursor_fav.fetchone()[0]
    print(f"COUNT(*): Total entries in favorites: {total_count}")

    # Count distinct languages
    cursor_fav.execute("SELECT COUNT(DISTINCT language) FROM favorites;")
    distinct_languages = cursor_fav.fetchone()[0]
    print(f"COUNT(DISTINCT language): Unique programming languages: {distinct_languages}")

    conn_fav.close()

    # 2. Aggregations on shows.db (numerical tables)
    print("\n=== Aggregations on shows.db (Ratings Table) ===")
    conn_shows = sqlite3.connect(SHOWS_DB)
    cursor_shows = conn_shows.cursor()

    # Calculate average, min, and max rating
    cursor_shows.execute("SELECT AVG(rating), MIN(rating), MAX(rating), SUM(votes) FROM ratings;")
    avg_r, min_r, max_r, total_v = cursor_shows.fetchone()
    print(f"AVG(rating):  Average show rating: {avg_r:.2f}")
    print(f"MIN(rating):  Lowest show rating:  {min_r:.1f}")
    print(f"MAX(rating):  Highest show rating: {max_r:.1f}")
    print(f"SUM(votes):   Total votes cast:    {total_v:,}")

    conn_shows.close()

if __name__ == "__main__":
    aggregation_examples()
