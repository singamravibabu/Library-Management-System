# This file is managed by Student 1
from database.db_connection import get_db_connection

class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies

    @staticmethod
    def add_book(title, author, isbn, total_copies):
        """Adds a new book to the database"""
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO books (title, author, isbn, total_copies, available_copies) VALUES (%s, %s, %s, %s, %s)"
            values = (title, author, isbn, total_copies, total_copies)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            print("Book added successfully!")

    @staticmethod
    def update_book(book_id, title=None, author=None, isbn=None, total_copies=None):
        """Updates book details in the database"""
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            updates = []
            values = []

            if title:
                updates.append("title = %s")
                values.append(title)
            if author:
                updates.append("author = %s")
                values.append(author)
            if isbn:
                updates.append("isbn = %s")
                values.append(isbn)
            if total_copies:
                updates.append("total_copies = %s")
                values.append(total_copies)

            if updates:
                query = f"UPDATE books SET {', '.join(updates)} WHERE book_id = %s"
                values.append(book_id)
                cursor.execute(query, values)
                conn.commit()

            conn.close()
            print("Book updated successfully!")

    @staticmethod
    def delete_book(book_id):
        """Deletes a book from the database"""
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            query = "DELETE FROM books WHERE book_id = %s"
            cursor.execute(query, (book_id,))
            conn.commit()
            conn.close()
            print("Book deleted successfully!")

    @staticmethod
    def get_all_books():
        """Retrieves all books from the database"""
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            query = "SELECT * FROM books"
            cursor.execute(query)
            books = cursor.fetchall()
            conn.close()
            return books

# Test the functionality
if __name__ == "__main__":
    Book.add_book("Python Programming", "John Doe", "1234567890", 5)
    books = Book.get_all_books()
    print(books)