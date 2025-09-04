# Module-2-Project
Library Management System - Project Report By Sukhada Inamdar
Note = Admin and Member password is admin123  
1. Project Overview
This project is a console-based Library Management System developed in Python. It simulates the operations of a library, such as managing books, registering members, issuing and returning books, and generating overdue reports. The system uses CSV files as a lightweight database and implements authentication with password hashing using bcrypt.
2. Learning Goals
• Design a mini-database using CSV files
• Model many-to-many relationships (Members ↔ Loans)
• Practice login systems, user roles, and password hashing
• Implement CRUD operations and due-date logic
3. System Roles
• Librarian: Add/delete books, register members, issue/return books, view overdue list
• Member: Search catalogue, check availability, view own loan history
4. File Schema
• books.csv: ISBN, Title, Author, CopiesTotal, CopiesAvailable
• members.csv: MemberID, Name, PasswordHash, Email, JoinDate
• loans.csv: LoanID, MemberID, ISBN, IssueDate, DueDate, ReturnDate
5. Step-by-Step Build Plan
• Setup: Create models and CSV storage helpers
• Auth: Register/login with bcrypt hashing
• Librarian Menu: Add, remove, issue, return, view overdue
• Member Menu: Search catalogue, view loans
• Business Rules: Issue (CopiesAvailable--), Return (CopiesAvailable++)
• Overdue Report: Show loans past due date
• Validation: Check for duplicates, invalid ISBNs, password mismatch
• Testing: Use pytest for issue-return
• CLI Support: Add --data-dir flag with argparse
6. Technology Stack
• Language: Python 3
• Libraries: bcrypt, csv, datetime, dataclasses
• Tools: pytest (for testing)
• Storage: CSV files
7. Console Snapshot
=== Librarian Dashboard ===
1. Add Book
2. Register Member
3. Issue Book
4. Return Book
5. Overdue List
6. Logout
> Example=
3
ISBN to issue: 9780132350884
Member ID: 1001
✔ Book issued. Due on 29-May-2025.
8. Conclusion
The Library Management System successfully implements the key features of a real-world library using a simple and accessible console interface. The project improves understanding of file handling, user authentication, and software design principles in Python.
 
