import pandas as pd
import sqlite3

# Step 1: Load the CSV files
bank_df = pd.read_csv('C:/Users/patienceben/Downloads/bank_transactions.csv')
processor_df = pd.read_csv('C:/Users/patienceben/Downloads/processor_transactions.csv')

# Step 2: Create SQLite DB and load data
conn = sqlite3.connect('reconciliation.db')
bank_df.to_sql('bank_transactions', conn, if_exists='replace', index=False)
processor_df.to_sql('processor_transactions', conn, if_exists='replace', index=False)

print("✅ Data loaded into SQLite database.")

# Step 3: Sample Queries

# 1. Transactions in bank but NOT in processor
print("\n🔍 Transactions in bank but NOT in processor:")
query1 = '''
SELECT * FROM bank_transactions b
LEFT JOIN processor_transactions p
ON b.reference_no = p.reference_no
WHERE p.reference_no IS NULL;
'''
print(pd.read_sql(query1, conn))

# 2. Transactions in processor but NOT in bank
print("\n🔍 Transactions in processor but NOT in bank:")
query2 = '''
SELECT * FROM processor_transactions p
LEFT JOIN bank_transactions b
ON p.reference_no = b.reference_no
WHERE b.reference_no IS NULL;
'''
print(pd.read_sql(query2, conn))

# 3. Amount mismatches
print("\n🔍 Transactions with amount mismatches:")
query3 = '''
SELECT b.transaction_id, b.reference_no,
       b.amount AS bank_amount,
       p.amount AS processor_amount
FROM bank_transactions b
JOIN processor_transactions p
ON b.reference_no = p.reference_no
WHERE b.amount != p.amount;
'''
print(pd.read_sql(query3, conn))

# 4. Status mismatches
print("\n🔍 Transactions with status mismatches:")
query4 = '''
SELECT b.transaction_id, b.reference_no,
       b.status AS bank_status,
       p.status AS processor_status
FROM bank_transactions b
JOIN processor_transactions p
ON b.reference_no = p.reference_no
WHERE b.status != p.status;
'''
print(pd.read_sql(query4, conn))

conn.close()
