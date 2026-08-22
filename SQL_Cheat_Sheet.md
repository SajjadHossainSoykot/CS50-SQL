# SQL Cheat Sheet & Reference Guide

This guide provides a quick reference for common SQL commands, structures, syntax, and Python `sqlite3` integration.

---

## 1. Core SQL Commands

| Command | Description | Example Query |
| :--- | :--- | :--- |
| **`SELECT`** | Specifies the columns to retrieve. | `SELECT language, problem FROM favorites;` |
| **`WHERE`** | Filters rows based on a specific boolean condition. | `SELECT * FROM favorites WHERE language = 'Python';` |
| **`LIKE`** | Filters text columns using wildcards (`%`). | `SELECT * FROM favorites WHERE problem LIKE 'Mario%';` |
| **`ORDER BY`** | Sorts the result set (default: `ASC`, use `DESC` for descending). | `SELECT * FROM ratings ORDER BY rating DESC;` |
| **`LIMIT`** | Constrains the maximum number of rows returned. | `SELECT * FROM shows LIMIT 5;` |
| **`GROUP BY`** | Groups duplicate row values together to perform aggregates. | `SELECT language, COUNT(*) FROM favorites GROUP BY language;` |
| **`HAVING`** | Filters groups created by `GROUP BY` (like `WHERE`, but for groups). | `SELECT genre, COUNT(*) FROM genres GROUP BY genre HAVING COUNT(*) > 100;` |
| **`JOIN`** / **`INNER JOIN`** | Combines columns from tables that share common keys. | `SELECT s.title, r.rating FROM shows s JOIN ratings r ON s.id = r.show_id;` |

---

## 2. SQL Aggregate Functions

Aggregate functions perform calculations on multiple values and return a single value.

*   `COUNT(*)`: Counts the total number of matching rows.
*   `AVG(column)`: Calculates the average of numerical column values.
*   `SUM(column)`: Calculates the sum of numerical column values.
*   `MIN(column)`: Finds the minimum value.
*   `MAX(column)`: Finds the maximum value.
*   `DISTINCT(column)`: Returns only unique, non-duplicate values of a column.

---

## 3. Subqueries (Nested Queries)

Subqueries allow you to nest a query inside another query's conditions.

```sql
-- Find titles of all shows written by Vince Gilligan
SELECT title FROM shows
WHERE id IN (
    SELECT show_id FROM writers
    WHERE person_id = (
        SELECT id FROM people
        WHERE name = 'Vince Gilligan'
    )
);
```

---

## 4. Python `sqlite3` Connection Template

A template for connecting to a database, executing parameterized queries, fetching results, and handling database errors safely.

```python
import sqlite3

# 1. Establish connection to the SQLite database
conn = sqlite3.connect("databases/favorites.db")
cursor = conn.cursor()

try:
    # 2. Define a parameterized query (SQL Injection safe)
    query = "SELECT * FROM favorites WHERE language = ? LIMIT ?;"
    params = ("Python", 5)

    # 3. Execute and fetch results
    cursor.execute(query, params)
    rows = cursor.fetchall()
    
    for row in rows:
        print(f"ID: {row[0]}, Time: {row[1]}, Language: {row[2]}, Problem: {row[3]}")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # 4. Always close the connection to clean up resources
    conn.close()
```
