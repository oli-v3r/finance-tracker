import csv
import os
from datetime import datetime

from transaction import Transaction

DATA_DIR = "data"
OUTPUT_DIR = "output"

PC_FILENAME = "report.csv"
WS_FILENAME = "ws.csv"  # rename your Wealthsimple export to this each time


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
            if row['transaction_type'] == 'Payment':
                continue
            if row['status'] != 'Completed':
                continue
            t = Transaction(
                date=datetime.strptime(row['transaction_date'], '%Y-%m-%d').strftime('%Y-%m-%d'),
                description=row['merchant'],
                amount=abs(float(row['amount'])),
                card='WS'
            )
            transactions.append(t)
    return transactions


def sort_by_date(transactions):
    return sorted(transactions, key=lambda t: t.date)


def build_output_filename(transactions):
    dates = [t.date for t in transactions]
    start, end = min(dates), max(dates)
    if start[:7] == end[:7]:  # same year-month, e.g. "2026-07"
        return f"output_{start[:7]}.csv"
    return f"output_{start}_to_{end}.csv"


def write_csv(transactions, filepath):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['date', 'card', 'description', 'amount'])
        for t in transactions:
            writer.writerow([t.date, t.card, t.description, t.amount])


def main():
    pc_path = os.path.join(DATA_DIR, PC_FILENAME)
    ws_path = os.path.join(DATA_DIR, WS_FILENAME)

    transactions = read_pc(pc_path) + read_ws(ws_path)
    transactions = sort_by_date(transactions)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_filename = build_output_filename(transactions)
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    write_csv(transactions, output_path)
    print(f"Wrote {len(transactions)} transactions to {output_path}")


if __name__ == "__main__":
    main()