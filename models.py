# models.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Book:
    ISBN: str
    Title: str
    Author: str
    CopiesTotal: int
    CopiesAvailable: int

@dataclass
class Member:
    MemberID: str
    Name: str
    PasswordHash: str
    Email: str
    JoinDate: str  # ISO: YYYY-MM-DD

@dataclass
class Loan:
    LoanID: int
    MemberID: str
    ISBN: str
    IssueDate: str
    DueDate: str
    ReturnDate: Optional[str]  # Empty string if not returned
