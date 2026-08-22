import csv
from cs50 import SQL

# Create/reset the empty database file so cs50.SQL can connect to it
open("favorites.db", "w").close()

# Connect to database
db = SQL("sqlite:///favorites.db")

# Create favorites table
db.execute("CREATE TABLE favorites (id INTEGER PRIMARY KEY AUTOINCREMENT, Timestamp TEXT, language TEXT, problem TEXT)")

# Open CSV file
with open("favorites.csv", "r") as file:
    # Create DictReader to parse headers as keys
    reader = csv.DictReader(file)

    # Iterate over CSV file, inserting each row into the database
    for row in reader:
        # Insert row into the SQL table
        db.execute(
            "INSERT INTO favorites (Timestamp, language, problem) VALUES (?, ?, ?)",
            row["Timestamp"],
            row["language"],
            row["problem"]
        )
