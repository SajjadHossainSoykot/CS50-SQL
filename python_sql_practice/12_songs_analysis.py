import os
import sqlite3

# Define database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SONGS_DB = os.path.join(BASE_DIR, "..", "databases", "songs.db")

def songs_analysis():
    """
    Demonstrates SQL analysis and relational queries on the songs database:
    1. Aggregation & Grouping: Top artists by track count and average energy
    2. Relational JOIN: Linking songs with artists to find top danceable hits
    3. Multi-Criteria Filtering: High-danceability and high-valence feel-good tracks
    4. Subquery: Identifying tracks produced by high-energy artists
    """
    print("Executing 12_songs_analysis.py...")

    conn = None
    try:
        conn = sqlite3.connect(SONGS_DB)
        cursor = conn.cursor()

        # Example 1: Top artists by number of tracks and average energy
        print("\n--- Example 1: Top Artists by Song Count & Average Energy ---")
        query_top_artists = """
        SELECT a.name, COUNT(s.id) AS song_count, ROUND(AVG(s.energy), 3) AS avg_energy
        FROM artists a
        JOIN songs s ON a.id = s.artist_id
        GROUP BY a.name
        HAVING song_count >= 3
        ORDER BY song_count DESC, avg_energy DESC;
        """
        cursor.execute(query_top_artists)
        for row in cursor.fetchall():
            print(f"- {row[0]}: {row[1]} songs | Avg Energy: {row[2]}")

        # Example 2: Relational JOIN - Top 5 Most Danceable Songs
        print("\n--- Example 2: Top 5 Most Danceable Songs ---")
        query_danceable = """
        SELECT s.name, a.name, s.danceability, s.tempo
        FROM songs s
        INNER JOIN artists a ON s.artist_id = a.id
        ORDER BY s.danceability DESC
        LIMIT 5;
        """
        cursor.execute(query_danceable)
        for row in cursor.fetchall():
            print(f"- \"{row[0]}\" by {row[1]} | Danceability: {row[2]} | Tempo: {row[3]:.1f} BPM")

        # Example 3: Multi-Criteria Filtering - High Valence & Danceability (Feel-Good Songs)
        print("\n--- Example 3: Feel-Good Songs (Danceability > 0.75 & Valence > 0.75) ---")
        query_feel_good = """
        SELECT s.name, a.name, s.danceability, s.valence
        FROM songs s
        JOIN artists a ON s.artist_id = a.id
        WHERE s.danceability > 0.75 AND s.valence > 0.75
        ORDER BY s.valence DESC
        LIMIT 5;
        """
        cursor.execute(query_feel_good)
        for row in cursor.fetchall():
            print(f"- \"{row[0]}\" by {row[1]} | Valence: {row[2]} | Danceability: {row[3]}")

        # Example 4: Subquery - Songs by artists whose average tempo exceeds 130 BPM
        print("\n--- Example 4: Songs by Fast-Paced Artists (Avg Tempo > 130 BPM) ---")
        query_subquery_tempo = """
        SELECT s.name, a.name, s.tempo
        FROM songs s
        JOIN artists a ON s.artist_id = a.id
        WHERE a.id IN (
            SELECT artist_id
            FROM songs
            GROUP BY artist_id
            HAVING AVG(tempo) > 130
        )
        ORDER BY s.tempo DESC
        LIMIT 5;
        """
        cursor.execute(query_subquery_tempo)
        for row in cursor.fetchall():
            print(f"- \"{row[0]}\" by {row[1]} | Tempo: {row[2]:.1f} BPM")

    except sqlite3.Error as e:
        print(f"An error occurred while querying songs.db: {e}")
    finally:
        if conn:
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    songs_analysis()
