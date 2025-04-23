# 💸 Spendora

**Spendora** is a personal expense tracker built with **Python** and **SQL**, designed to help you develop solid budgeting habits while practicing my coding skills. Track your spending, analyze your habits, and grow the app every week — all while sharpening your backend and data-handling abilities.

> Start simple, build weekly. Spendora is the financial assistant you code yourself.

---

## 📦 Features

- Record daily expenses with categories and payment methods
- View transactions filtered by date or category
- Summarize monthly and category-wise spending
- Store data securely in an SQLite database (easily swappable for PostgreSQL)
- Designed to grow — perfect for adding new features every Wednesday

---

## 🛠 Tech Stack

- **Python 3.10+**
- **SQLite** (lightweight embedded database)
- **Matplotlib** or **Seaborn** (for optional future charts)
- **Pandas** (for data analysis and exports)
- CLI-based interface (with potential for web version later)

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/spendora.git
cd spendora

## Project Structure
spendora/
├── main.py               # CLI entry point
├── db/
│   ├── init_db.py        # Database schema setup
│   └── connection.py     # Connection & DB utilities
├── models/
│   ├── transaction.py    # Expense logic
│   └── category.py       # Category handling
├── reports/
│   ├── summary.py        # Analytics and summaries
│   └── charts.py         # Visualizations (coming soon)
├── tests/
│   └── test_transactions.py
├── requirements.txt
└── README.md

## Why “Spendora”?
Like Pandora’s box, Spendora reveals your financial patterns — but with clarity and insight, not chaos. Open it every week and unlock smarter spending habits.


