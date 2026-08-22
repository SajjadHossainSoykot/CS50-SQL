import os
import subprocess

# Reset/remove the existing database file to start clean
if os.path.exists("favorites.db"):
    os.remove("favorites.db")

# Define SQLite CLI commands to import the CSV while keeping the autoincrement ID
commands = """
.mode csv
.import favorites.csv temp_favorites

CREATE TABLE favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Timestamp TEXT,
    language TEXT,
    problem TEXT
);

INSERT INTO favorites (Timestamp, language, problem)
SELECT Timestamp, language, problem FROM temp_favorites;

DROP TABLE temp_favorites;
"""

# Run the SQLite CLI commands
subprocess.run(["sqlite3", "favorites.db"], input=commands, text=True)

print("Database favorites.db successfully populated using SQLite CLI!")
