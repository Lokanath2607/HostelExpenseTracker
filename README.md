# Hostel Expense Tracker

A Python + SQLite project to manage and analyze hostel expenses.  
This project demonstrates database design, SQL queries, automation, and integration with Excel dashboards.

---

## 🚀 Features
- Relational schema for **Students** and **Expenses** tables with foreign key constraints.
- Automated SQL queries for:
  - Category breakdown (Food, Rent, Utilities, Misc).
  - Monthly spending per student.
  - Highest spender analysis.
- CSV export for easy visualization in Excel or Google Sheets.
- End‑to‑end workflow: database design → query execution → reporting.

---

## 🛠 Tech Stack
- **Python 3**
- **SQLite**
- **CSV / Excel** for reporting

---

## 📂 Project Structure
HostelExpenseTracker/
│-- main.py              # Python script with database + queries
│-- hostel.db            # SQLite database (auto‑created)
│-- category_breakdown.csv
│-- monthly_spending.csv
│-- highest_spender.csv
│-- README.md             # Project documentation


---

## ▶️ How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/Lokanath2607/HostelExpenseTracker.git
   cd HostelExpenseTracker
2. Run the script:
   python main.py
3. Open the generated CSV files in Excel to build dashboards.

📊 Example Output
Category Breakdown

Highest Spender → Lokanath (₹7300)
