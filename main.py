import datetime

class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
        self.available_copies = copies

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.transactions = []

    def add_book(self, book_id, title, author, copies):
        book = Book(book_id, title, author, copies)
        self.books.append(book)

    def add_user(self, user_id, name):
        user = User(user_id, name)
        self.users.append(user)

    def borrow_book(self, user_id, book_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.book_id == book_id and b.available_copies > 0), None)

        if user and book:
            user.books_borrowed.append(book)
            book.available_copies -= 1
            transaction = {
                'user_id': user_id,
                'book_id': book_id,
                'action': 'Borrow',
                'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            self.transactions.append(transaction)
            print(f"Book '{book.title}' borrowed by {user.name}")
        else:
            print("Book not available or user not found.")

    def return_book(self, user_id, book_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        book = next((b for b in self.books if b.book_id == book_id), None)

        if user and book and book in user.books_borrowed:
            user.books_borrowed.remove(book)
            book.available_copies += 1
            transaction = {
                'user_id': user_id,
                'book_id': book_id,
                'action': 'Return',
                'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            self.transactions.append(transaction)
            print(f"Book '{book.title}' returned by {user.name}")
        else:
            print("Book not borrowed by the user or user not found.")

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print(f"{book.book_id}. {book.title} by {book.author} - Available copies: {book.available_copies}")

    def display_users(self):
        print("Users in the library:")
        for user in self.users:
            print(f"{user.user_id}. {user.name}")

    def display_transactions(self):
        print("Transaction history:")
        for transaction in self.transactions:
            action = "Borrowed" if transaction['action'] == 'Borrow' else "Returned"
            print(f"{transaction['date']} - User {transaction['user_id']} {action} book {transaction['book_id']}")

# Example usage
library_system = LibraryManagementSystem()

# Add books and users
library_system.add_book(1, 'The Great Gatsby', 'F. Scott Fitzgerald', 5)
library_system.add_book(2, 'To Kill a Mockingbird', 'Harper Lee', 3)
library_system.add_user(101, 'John Doe')
library_system.add_user(102, 'Jane Smith')

# Borrow and return books
library_system.borrow_book(101, 1)
library_system.borrow_book(102, 1)
library_system.borrow_book(101, 2)
library_system.return_book(101, 1)

# Display information
library_system.display_books()
library_system.display_users()
library_system.display_transactions()
