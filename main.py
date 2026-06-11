import sqlite3
import csv

# Connect to database (creates hostel.db file)
conn = sqlite3.connect("hostel.db")
cur = conn.cursor()

# Create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS Students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    room_no INTEGER
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Expenses (
    expense_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    category TEXT,
    amount REAL,
    expense_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
)
""")
# Clear old data so we don't get duplicate IDs
cur.execute("DELETE FROM Students")
cur.execute("DELETE FROM Expenses")

# Insert sample data
cur.executemany("INSERT INTO Students VALUES (?, ?, ?)", [
    (1, 'Lokanath', 1001),
    (2, 'Nandhini', 1002),
    (3, 'Kiran', 1003)
])

cur.executemany("INSERT INTO Expenses VALUES (?, ?, ?, ?, ?)", [
    (1, 1, 'Food', 2500, '2026-05-01'),
    (2, 1, 'Rent', 4000, '2026-05-01'),
    (3, 1, 'Utilities', 800, '2026-05-02'),
    (4, 2, 'Food', 2300, '2026-05-01'),
    (5, 2, 'Rent', 4000, '2026-05-01'),
    (6, 3, 'Misc', 1200, '2026-05-03')
])

conn.commit()

# --- Export Queries to CSV ---

# 1. Category Breakdown
cur.execute("SELECT category, SUM(amount) FROM Expenses GROUP BY category")
rows = cur.fetchall()
with open("category_breakdown.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Category", "Total Spent"])
    writer.writerows(rows)

# 2. Monthly Spending per Student
cur.execute("""
SELECT student_id, strftime('%Y-%m', expense_date) AS month,
       SUM(amount) AS total_spent
FROM Expenses
GROUP BY student_id, month
ORDER BY month
""")
rows = cur.fetchall()
with open("monthly_spending.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Student ID", "Month", "Total Spent"])
    writer.writerows(rows)

# 3. Highest Spender
cur.execute("""
SELECT s.name, SUM(e.amount) AS total_spent
FROM Students s
JOIN Expenses e ON s.student_id = e.student_id
GROUP BY s.name
ORDER BY total_spent DESC
LIMIT 1
""")
rows = cur.fetchall()
with open("highest_spender.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Total Spent"])
    writer.writerows(rows)

conn.close()
print("CSV files created: category_breakdown.csv, monthly_spending.csv, highest_spender.csv")
