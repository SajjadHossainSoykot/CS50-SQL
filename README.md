# CS50 SQL (Week 7 Experiments & Lecture Notes)

This repository contains python scripts, SQL databases, and data processing files from **CS50 Introduction to Computer Science - Week 7 (SQL)**. It demonstrates how to transition from flat-file data processing (CSVs) in Python to relational databases (SQLite) and structured query languages (SQL).

---

## 📂 Repository Structure

The project is structured into two main directories:

*   **[favorites/](favorites/)**: Demonstrates the step-by-step evolution of parsing, filtering, sorting, and querying a survey dataset in both Python and SQL.
*   **[imdb/](imdb/)**: Contains a large SQLite database `shows.db` representing a subset of IMDb’s data, used for practice queries.

---

## 📊 The Favorites Experiments

This experiment tracks responses about students' favorite programming languages (Python, C, Scratch) and favorite problems. The data is initially stored in [favorites.csv](favorites/favorites.csv) and undergoes a step-by-step processing evolution:

### 1. File Handling & CSV Parsing
*   **[favorites0.py](favorites/favorites0.py)**: Basic CSV reading using `csv.reader` and indexing.
*   **[favorites1.py](favorites/favorites1.py)**: Introduces basic variable storage for data mapping.
*   **[favorites2.py](favorites/favorites2.py)** & **[favorites3.py](favorites/favorites3.py)**: Parses CSV data using `csv.DictReader` to reference columns by name rather than index.

### 2. Data Aggregation & Counting (Python)
*   **[favorites4.py](favorites/favorites4.py)**: Counts favorite languages using simple `if/elif` statements.
*   **[favorites5.py](favorites/favorites5.py)**: Optimizes counting using a standard Python dictionary `counts`.
*   **[favorites6.py](favorites/favorites6.py)**: Implements error handling using `try/except KeyError` to initialize/increment dictionary values.

### 3. Sorting Data (Python)
*   **[favorites7.py](favorites/favorites7.py)**: Sorts and displays languages alphabetically using `sorted()`.
*   **[favorites8.py](favorites/favorites8.py)**: Sorts languages by popularity (value counts) in descending order using `sorted(counts, key=counts.get, reverse=True)`.

### 4. Transitioning to SQL
*   **[csv_to_db.py](favorites/csv_to_db.py)**: Script that reads [favorites.csv](favorites/favorites.csv), creates an empty database `favorites.db`, defines a `favorites` table, and inserts all CSV records into SQL.
*   **[favorites9.py](favorites/favorites9.py)**: Connects to `favorites.db` using the `cs50` library and executes a SQL aggregation query:
    ```sql
    SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC
    ```
*   **[favorites10.py](favorites/favorites10.py)**: Implements user-parameterized queries to prevent SQL injections using placeholders (`?`).

---

## 🎬 The IMDB Database

Located in the [imdb/](imdb/) directory, `shows.db` is a comprehensive database containing information about television shows. It includes tables for:
*   `shows` (id, title, year, episodes)
*   `genres` (show_id, genre)
*   `stars` (show_id, person_id)
*   `writers` (show_id, person_id)
*   `ratings` (show_id, rating, votes)
*   `people` (id, name, birth)

You can explore and query this database using SQLite in the command line:
```bash
sqlite3 imdb/shows.db
```

---

## ⚙️ Running the Files

### Setup
Ensure you have the required `cs50` library installed:
```bash
pip install cs50
```

### Execution
Always run the scripts from the directory containing their relative assets (`favorites/`) to avoid path errors:
```bash
cd favorites
python3 csv_to_db.py
python3 favorites9.py
```

### IDE Configuration
If you run scripts in VS Code using the play button or Code Runner, the workspace has been configured in [.vscode/settings.json](.vscode/settings.json) to execute python files within their file's directory:
```json
{
  "code-runner.fileDirectoryAsCwd": true,
  "python.terminal.executeInFileDir": true
}
```
