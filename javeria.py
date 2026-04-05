
# Book class
class Book:
    def _init_(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def label(self):
        return f"{self.title} by {self.author} ({self.book_id})"


# Member class
class Member:
    def _init_(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed = set()  # books currently borrowed

    def can_borrow(self, max_loans):
        return len(self.borrowed) < max_loans


# Library class
class Library:
    def _init_(self, max_loans=3):
        self.max_loans = max_loans
        self.books = {}    # book_id -> Book
        self.members = {}  # member_id -> Member
        self.loans = {}    # book_id -> (member_id, due_days)

    def add_book(self, book):
        if book.book_id in self.books:
            print(f"Book {book.book_id} already exists!")
        else:
            self.books[book.book_id] = book

    def register_member(self, member):
        if member.member_id in self.members:
            print(f"Member {member.member_id} already exists!")
        else:
            self.members[member.member_id] = member

    def borrow(self, book_id, member_id, due_days=14):
        if book_id not in self.books:
            print("Book not found.")
            return
        if member_id not in self.members:
            print("Member not found.")
            return
        if book_id in self.loans:
            print("Book is already borrowed.")
            return

        member = self.members[member_id]
        if not member.can_borrow(self.max_loans):
            print("Member reached max loan limit.")
            return

        # Borrow the book
        self.loans[book_id] = (member_id, due_days)
        member.borrowed.add(book_id)
        print(f"{member.name} borrowed {self.books[book_id].title} for {due_days} days.")

    def return_book(self, book_id):
        if book_id not in self.loans:
            print("This book is not borrowed.")
            return
        member_id, _ = self.loans.pop(book_id)
        self.members[member_id].borrowed.remove(book_id)
        print(f"{self.books[book_id].title} returned successfully.")

    def list_available(self):
        print("Available books:")
        for book_id, book in self.books.items():
            if book_id not in self.loans:
                print("-", book.label())

    def member_loans(self, member_id):
        if member_id not in self.members:
            print("Member not found.")
            return
        member = self.members[member_id]
        print(f"{member.name}'s borrowed books:")
        for book_id in member.borrowed:
            _, due = self.loans[book_id]
            print(f"- {self.books[book_id].label()}, due in {due} days")



if __name__ == "_main_":
    lib = Library(max_loans=2)

    # Add books
    lib.add_book(Book("B001", "Clean Code", "Robert C. Martin"))
    lib.add_book(Book("B002", "Python Crash Course", "Eric Matthes"))
    lib.add_book(Book("B003", "The Pragmatic Programmer", "Andrew Hunt"))

    # Register members
    lib.register_member(Member("M001", "Ayesha"))
    lib.register_member(Member("M002", "Hassan"))

    # Borrow books
    lib.borrow("B001", "M001", due_days=7)
    lib.borrow("B002", "M001")

    # List available books
    lib.list_available()

    # Show member loans
    lib.member_loans("M001")

    # Return a book
    lib.return_book("B001")
    lib.list_available()# class A:
