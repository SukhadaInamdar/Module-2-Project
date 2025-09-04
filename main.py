# main.py
from auth import login, register_member, session
from librarian import add_book, remove_book, issue_book, return_book, view_overdue
from member import search_catalogue, my_loans

def librarian_menu():
    while True:
        print("\n=== Librarian Dashboard ===")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Overdue List")
        print("6. Logout")
        choice = input("> ")
        if choice == "1":
            add_book()
        elif choice == "2":
            register_member()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_overdue()
        elif choice == "6":
            break
        else:
            print("❌ Invalid choice.")

def member_menu():
    while True:
        print("\n=== Member Dashboard ===")
        print("1. Search Catalogue")
        print("2. My Loans")
        print("3. Logout")
        choice = input("> ")
        if choice == "1":
            search_catalogue()
        elif choice == "2":
            my_loans()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice.")

def main():
    print("=== Welcome to the Library System ===")
    print("Login as:\n1. Librarian\n2. Member")
    role = input("> ")
    if role == "1":
        if login("librarian"):
            librarian_menu()
    elif role == "2":
        if login("member"):
            member_menu()
    else:
        print("❌ Invalid role.")

if __name__ == "__main__":
    main()
