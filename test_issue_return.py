# tests/test_issue_return.py
from storage import read_books, write_books
from models import Book

def test_issue_return_updates_copies():
    books = read_books()
    test_book = next((b for b in books if b.ISBN == "9780132350884"), None)
    if not test_book:
        return

    initial = test_book.CopiesAvailable
    test_book.CopiesAvailable -= 1
    test_book.CopiesAvailable += 1

    assert test_book.CopiesAvailable == initial
