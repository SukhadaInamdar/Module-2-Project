# librarian.py
from storage import read_books, write_books, read_loans, write_loans, read_members
from auth import register_member
from models import Book, Loan
from utils import today, add_days, generate_loan_id

def add_book():
    books = read_books()
    isbn = input("ISBN: ")
    if any(b.ISBN == isbn for b in books):
        print("❌ ISBN already exists.")
        return
    title = input("Title: ")
    author = input("Author: ")
    total = int(input("Total Copies: "))
    if total < 0:
        print("❌ Copies cannot be negative.")
        return
    book = Book(isbn, title, author, total, total)
    books.append(book)
    write_books(books)
    print("✅ Book added.")

def remove_book():
    books = read_books()
    isbn = input("ISBN to remove: ")
    books = [b for b in books if b.ISBN != isbn]
    write_books(books)
    print("✅ Book removed if it existed.")

def issue_book():
    books = read_books()
    members = read_members()
    loans = read_loans()
    
    isbn = input("ISBN to issue: ")
    member_id = input("Member ID: ")

    book = next((b for b in books if b.ISBN == isbn), None)
    member = next((m for m in members if m.MemberID == member_id), None)

    if not book:
        print("❌ Book not found.")
        return
    if not member:
        print("❌ Member not found.")
        return
    if book.CopiesAvailable < 1:
        print("❌ No copies available.")
        return

    book.CopiesAvailable -= 1
    write_books(books)

    issue_date = today().isoformat()
    due_date = add_days(issue_date, 14)
    loan = Loan(generate_loan_id(loans), member_id, isbn, issue_date, due_date, "")
    loans.append(loan)
    write_loans(loans)
    print(f"✔ Book issued. Due on {due_date}.")

def return_book():
    loans = read_loans()
    books = read_books()

    loan_id = int(input("Loan ID to return: "))
    loan = next((l for l in loans if l.LoanID == loan_id and not l.ReturnDate), None)
    if not loan:
        print("❌ Active loan not found.")
        return

    loan.ReturnDate = today().isoformat()
    for b in books:
        if b.ISBN == loan.ISBN:
            b.CopiesAvailable += 1
            break

    write_books(books)
    write_loans(loans)
    print("✔ Book returned successfully.")

def view_overdue():
    loans = read_loans()
    members = read_members()
    overdue = [l for l in loans if not l.ReturnDate and l.DueDate < today().isoformat()]
    if not overdue:
        print("✅ No overdue books.")
        return

    print("=== Overdue Loans ===")
    for l in overdue:
        member = next((m for m in members if m.MemberID == l.MemberID), None)
        print(f"Loan ID: {l.LoanID}, Member: {member.Name if member else l.MemberID}, "
              f"ISBN: {l.ISBN}, Due: {l.DueDate}")
