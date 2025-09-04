# utils.py
from datetime import datetime, timedelta

def today():
    return datetime.now().date()

def add_days(date_str, days):
    d = datetime.strptime(date_str, "%Y-%m-%d").date()
    return (d + timedelta(days=days)).isoformat()

def generate_loan_id(loans):
    if not loans:
        return 1
    return max(loan.LoanID for loan in loans) + 1
