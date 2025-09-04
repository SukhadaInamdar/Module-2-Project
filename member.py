# member.py
from storage import read_books, read_loans
from auth import session
from models import Loan

def search_catalogue():
    books = read_books()
    query = input("Enter title/author keyword: ").lower()
    found = [b for b in books if query in b.Title.lower() or query in b.Author.lower()]
    if not found:
        print("❌ No books found.")
        return
    for b in found:
        print(f"{b.Title} by {b.Author} | ISBN: {b.ISBN} | Available: {b.CopiesAvailable}")

def my_loans():
    loans = read_loans()
    user_loans = [l for l in loans if l.MemberID == session["user"]]
    if not user_loans:
        print("ℹ️ No loans found.")
        return
    print("=== My Loan History ===")
    for l in user_loans:
        status = "Returned" if l.ReturnDate else "Active"
        print(f"LoanID: {l.LoanID}, ISBN: {l.ISBN}, Issued: {l.IssueDate}, Due: {l.DueDate}, Status: {status}")
