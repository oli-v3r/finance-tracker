from transaction import Transaction
import csv
from datetime import datetime


def read_pc(filepath):
    transactions = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Type'] == 'PAYMENT':
                continue
            t = Transaction(
                date=datetime.strptime(row['Date'], '%m/%d/%Y').strftime('%Y-%m-%d'),
                description=row['Description'],
                amount=abs(float(row['Amount'])),
                card='PC'
            )
            transactions.append(t)
    return transactions

def read_ws(filepath):
    transactions = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['type'] == 'Payment':
                continue
            t = Transaction(
                date=row['transaction_date'],
                description=row['details'],
                amount=abs(float(row['amount'])),
                card='WS'
            )
            transactions.append(t)
    return transactions

    


t1 = Transaction("2026-01-15", "Tim Hortons", 4.75, "PC")
t2 = Transaction("2026-01-18", "Whole Foods", 87.32, "WS")

print(t1)
print(t2)
print(t1.amount)