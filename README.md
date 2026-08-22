# CS50 SQL Learning Portfolio

Welcome to my CS50 SQL Learning Portfolio! This repository contains a structured, clean, and highly organized compilation of database experiments, scripts, and interactive notebooks demonstrating SQL concepts taught in CS50's Week 7 (SQL).

The portfolio shows how to transition from flat-file data processing (CSVs) to relational databases (SQLite) and structured query languages (SQL) using Python's native `sqlite3` library and the `pandas` library.

---

## 📂 Repository Structure

The project is organized as follows:

```text
project_root/
├── data/
│   └── favorites.csv               # Raw survey dataset containing student responses
│
├── databases/
│   ├── favorites.db                # SQLite database generated from favorites.csv
│   └── shows.db                    # IMDb television shows relational database (63.8 MB)
│
├── python_sql_practice/
│   ├── archive/                    # Original CS50 lecture python files
│   ├── database_connection.py      # Safe database connection & error handling template
│   ├── create_tables.py            # Creating database schemas & constraints (NOT NULL, CHECK)
│   ├── insert_examples.py          # Inserting records securely using parameterized queries
│   ├── select_examples.py          # Standard queries (SELECT, SELECT specific columns)
│   ├── filtering_examples.py       # Row filtering queries (WHERE, LIKE pattern matching)
│   ├── aggregation_examples.py     # Aggregation functions (COUNT, DISTINCT, AVG, MIN, MAX)
│   ├── grouping_examples.py        # Grouping and group-filtering aggregates (GROUP BY, HAVING)
│   ├── ordering_examples.py        # Sorting and bounding queries (ORDER BY, LIMIT)
│   ├── subquery_examples.py        # Nested queries (subqueries inside WHERE statements)
│   └── join_examples.py            # Multi-table relation queries (INNER JOINs)
│
├── notebooks/
│   ├── 01_SQL_Basics.ipynb         # Interactive walkthrough of core SELECT & WHERE operations
│   ├── 02_Favorites_Database.ipynb # Analytics & visual bar charts on programming languages
│   ├── 03_Songs_Database.ipynb     # Documented placeholder explaining songs schema
│   ├── 04_IMDb_Relationships.ipynb # Relational join queries & genre rating graphs on shows.db
│   └── SQL_Cheat_Sheet.ipynb       # Interactive reference guide of syntax rules & code blocks
│
├── csv_to_sqlite.py                # Standalone script converting CSV data to SQLite DB
└── README.md                       # This portfolio documentation
```

---

## 🎓 SQL Concepts Implemented

### 1. SELECT and WHERE
*   Retrieving column subsets and filtering matching rows.
*   *Example Query:*
    ```sql
    SELECT language, problem FROM favorites WHERE language = 'Python' LIMIT 5;
    ```

### 2. LIKE (Pattern Matching)
*   Finding partial string matches using wildcards (`%`).
*   *Example Query:*
    ```sql
    SELECT * FROM favorites WHERE problem LIKE 'Mario%';
    ```

### 3. ORDER BY & LIMIT
*   Sorting result rows alphabetically or numerically and restricting output count.
*   *Example Query:*
    ```sql
    SELECT s.title, r.rating FROM shows s
    INNER JOIN ratings r ON s.id = r.show_id
    ORDER BY r.rating DESC LIMIT 10;
    ```

### 4. Aggregations (COUNT, AVG, MIN, MAX, SUM)
*   Running calculations on groups of numbers or rows.
*   *Example Query:*
    ```sql
    SELECT AVG(rating), MAX(rating) FROM ratings;
    ```

### 5. GROUP BY & HAVING
*   Splitting table rows into groups based on column values and filtering those groups.
*   *Example Query:*
    ```sql
    SELECT genre, COUNT(*) AS count
    FROM genres
    GROUP BY genre
    HAVING count > 10000;
    ```

### 6. Subqueries
*   Nesting a `SELECT` statement inside another query.
*   *Example Query:*
    ```sql
    SELECT title FROM shows
    WHERE id IN (
        SELECT show_id FROM writers
        WHERE person_id = (SELECT id FROM people WHERE name = 'Vince Gilligan')
    );
    ```

### 7. INNER JOINs (Relational Mapping)
*   Combining columns from multiple tables by matching their shared keys.
*   *Example Query:*
    ```sql
    SELECT p.name, s.title
    FROM people p
    INNER JOIN stars st ON p.id = st.person_id
    INNER JOIN shows s ON st.show_id = s.id
    WHERE s.title = 'Breaking Bad';
    ```

---

## 💾 Database Schemas

### 1. Favorites Database (`favorites.db`)
```sql
CREATE TABLE favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Timestamp TEXT,
    language TEXT,
    problem TEXT
);
```

### 2. IMDb Television Database (`shows.db`)
*   **`shows`** (`id` PRIMARY KEY, `title`, `year`, `episodes`)
*   **`genres`** (`show_id` FOREIGN KEY, `genre`)
*   **`ratings`** (`show_id` UNIQUE FOREIGN KEY, `rating`, `votes`)
*   **`people`** (`id` PRIMARY KEY, `name`, `birth`)
*   **`stars`** (`show_id` FOREIGN KEY, `person_id` FOREIGN KEY)
*   **`writers`** (`show_id` FOREIGN KEY, `person_id` FOREIGN KEY)

---

## ⚙️ How to Run & Explore

### Prerequisites
Install the required packages (`pandas` and `matplotlib` for Jupyter Notebooks):
```bash
pip install pandas matplotlib
```

### 1. Rebuild the Database from CSV
If you want to regenerate `databases/favorites.db` from the source CSV file, run the root converter:
```bash
python3 csv_to_sqlite.py
```

### 2. Execute Python Scripts
To run the educational SQL scripts inside the practice folder:
```bash
python3 python_sql_practice/database_connection.py
python3 python_sql_practice/filtering_examples.py
python3 python_sql_practice/join_examples.py
```

### 3. Open Interactive Notebooks
Start Jupyter Lab/Notebook from the project directory:
```bash
jupyter notebook
```
Navigate to `notebooks/` and run the cells in:
*   `01_SQL_Basics.ipynb` to learn query filters.
*   `02_Favorites_Database.ipynb` to see language distribution charts.
*   `04_IMDb_Relationships.ipynb` to analyze television genre metrics.

---

## 🔒 Safety Statement
To keep this repository educational and safe:
*   No script or notebook contains destructive commands such as `DELETE`, `DROP TABLE`, or `DROP DATABASE`.
*   All data inserts utilize SQL **parameterization** (`?` placeholders) to prevent SQL injection vulnerabilities.
