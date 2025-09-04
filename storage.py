# storage.py
import csv
import os
from models import Book, Member, Loan

DATA_DIR = "./data"

def get_csv_path(filename):
    return os.path.join(DATA_DIR, filename)

def read_books():
    with open(get_csv_path("books.csv"), newline='') as f:
        return [Book(row["ISBN"], row["Title"], row["Author"],
                     int(row["CopiesTotal"]), int(row["CopiesAvailable"]))
                for row in csv.DictReader(f)]

def write_books(books):
    with open(get_csv_path("books.csv"), "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["ISBN", "Title", "Author", "CopiesTotal", "CopiesAvailable"])
        writer.writeheader()
        for b in books:
            writer.writerow(b.__dict__)

def read_members():
    with open(get_csv_path("members.csv"), newline='') as f:
        return [Member(**row) for row in csv.DictReader(f)]

def write_members(members):
    with open(get_csv_path("members.csv"), "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["MemberID", "Name", "PasswordHash", "Email", "JoinDate"])
        writer.writeheader()
        for m in members:
            writer.writerow(m.__dict__)

def read_loans():
    with open(get_csv_path("loans.csv"), newline='') as f:
        return [Loan(int(row["LoanID"]), row["MemberID"], row["ISBN"],
                     row["IssueDate"], row["DueDate"], row["ReturnDate"])
                for row in csv.DictReader(f)]

def write_loans(loans):
    with open(get_csv_path("loans.csv"), "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["LoanID", "MemberID", "ISBN", "IssueDate", "DueDate", "ReturnDate"])
        writer.writeheader()
        for l in loans:
            writer.writerow({
                "LoanID": l.LoanID,
                "MemberID": l.MemberID,
                "ISBN": l.ISBN,
                "IssueDate": l.IssueDate,
                "DueDate": l.DueDate,
                "ReturnDate": l.ReturnDate or ""
            })
