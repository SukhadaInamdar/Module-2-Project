# auth.py
import bcrypt
from getpass import getpass
from storage import read_members, write_members
from models import Member
from datetime import date

session = {}

def register_member():
    members = read_members()
    member_id = input("Member ID: ")
    if any(m.MemberID == member_id for m in members):
        print("❌ Member ID already exists.")
        return
    name = input("Name: ")
    email = input("Email: ")
    pw = getpass("Password: ")
    confirm_pw = getpass("Confirm Password: ")
    if pw != confirm_pw:
        print("❌ Passwords do not match.")
        return
    hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
    m = Member(member_id, name, hashed, email, date.today().isoformat())
    members.append(m)
    write_members(members)
    print("✅ Member registered successfully.")

def login(role):
    members = read_members()
    if role == "librarian":
        pw = getpass("Enter librarian password: ")
        if pw == "admin123":  # Hardcoded for demo
            session["role"] = "librarian"
            session["user"] = "LIB001"
            return True
        else:
            print("❌ Invalid librarian password.")
            return False
    else:
        member_id = input("Member ID: ")
        pw = getpass("Password: ")
        for m in members:
            if m.MemberID == member_id and bcrypt.checkpw(pw.encode(), m.PasswordHash.encode()):
                session["role"] = "member"
                session["user"] = m.MemberID
                print(f"✅ Welcome {m.Name}!")
                return True
        print("❌ Login failed.")
        return False
