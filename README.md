# Finance Tracker

A Python tool for consolidating personal credit card transactions from multiple sources into a single, cleaned, sorted CSV.

## Overview

Reads transaction exports from PC Financial and Wealthsimple credit cards, normalizes them into a common format, filters out payments and pending charges, and writes a single sorted CSV for personal budgeting.

## Project Structure

```
finance-tracker/
├── data/          # Input CSVs (gitignored - not committed)
├── output/        # Cleaned output CSVs (gitignored - not committed)
├── main.py        # Main pipeline
├── transaction.py # Transaction class
└── README.md
```

## Input Files

Export date ranges directly from each provider (no manual month filtering needed) and place both files in `/data`:

| Card | Expected filename | Notes |
|------|-------------------|-------|
| PC Financial | `report.csv` | Default export name, used as-is |
| Wealthsimple | `ws.csv` | Rename the exported file to this each time |

**PC Financial** columns: `Date, Description, Amount, Type` — rows with `Type == PAYMENT` are dropped.

**Wealthsimple** columns: `transaction_date, transaction_type, status, merchant, amount, currency, notes, category` — rows with `transaction_type == Payment` or `status != Completed` are dropped (pending charges are excluded until they settle).

## Usage

```bash
python3 main.py
```

Output is written to `/output` as `output_<YYYY-MM>.csv` if all transactions fall in one month, or `output_<start-date>_to_<end-date>.csv` if the data spans multiple months.

Output columns: `date, card, description, amount`

## Built With

- Python 3.10
- csv, datetime, os (standard library)