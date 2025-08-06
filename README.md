# 🧾 Transaction Reconciliation SQL Project

This project simulates a real-world transaction reconciliation process using SQL and Python. It compares bank transactions with payment processor data to detect mismatches, missing records, and other inconsistencies.

## 📂 Dataset

Two CSV files were used:
- `bank_transactions.csv`
- `processor_transactions.csv`

Each contains:
- `transaction_id`
- `transaction_date`
- `amount`
- `status`
- `reference_no`
- `description`

## 🧠 Skills Demonstrated

- SQL querying with `JOIN`, `LEFT JOIN`, `CASE`, and filtering
- Data cleaning and comparison
- Python (pandas, sqlite3)
- Real-world reconciliation logic
- Error handling and debugging

## 🔍 Key Checks Performed

- Transactions in bank but not in processor ✅
- Transactions in processor but not in bank ✅
- Amount mismatches ✅
- Status mismatches ✅

## 🧪 How to Run

1. Ensure Python + pandas is installed
2. Place all files in the same directory
3. Run:

```bash
reconciliation_project.py


