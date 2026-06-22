# Finance Tracker

A Python tool for consolidating and filtering personal credit card transactions from multiple sources into a single cleaned CSV.

## Overview

Reads transaction exports from PC Financial and Wealthsimple credit cards, filters by month, and outputs a sorted, normalized CSV for personal budgeting.

## Project Structure

finance-tracker/
├── data/          # Input CSVs (gitignored - not committed)
├── output/        # Cleaned output CSVs (gitignored - not committed)
├── main.py        # Main pipeline
├── transaction.py # Transaction class
└── README.md

## Usage

Add your exported CSVs to the /data folder, then run:

```bash
python3 main.py
```

## Built With

- Python 3.10
- csv, datetime (standard library)