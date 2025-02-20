# This file is managed by Student 3
from database.db_connection import get_db_connection
from datetime import date

class Transaction:
    @staticmethod
    def issue_book(book_id, member_id):
        """Issues a book to a member if available"""
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            
            # Check if the book is available
            cursor.execute("SELECT available_copies FROM books WHERE book_id = %s", (book_id,))
            book = cursor.fetchone()
            
            if book and book[0] > 0:
                # Issue the book
                query = "INSERT INTO transactions (book_id, member_id, issue_date, status) VALUES (%s, %s, %s, 'issued')"
                values = (book_id, member_id, date.today())
                cursor.execute(query, values)

                # Reduce available copies
                cursor.execute("UPDATE books SET available_copies = available_copies - 1 WHERE book_id = %s", (book_id,))
                
                conn.commit()
                conn.close()
                print("Book issued successfully!")
            else:
                print("Book not available for issue.")

    @staticmethod
    def return_book(transaction_id):
        """Marks a book as returned and updates availability"""
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            
            # Get book_id from transaction
            cursor.execute("SELECT book_id FROM transactions WHERE transaction_id = %s AND status = 'issued'", (transaction_id,))
            transaction = cursor.fetchone()
            
            if transaction:
                book_id = transaction[0]
                
                # Update transaction status
                cursor.execute("UPDATE transactions SET return_date = %s, status = 'returned' WHERE transaction_id = %s",
                               (date.today(), transaction_id))
                
                # Increase available copies
                cursor.execute("UPDATE books SET available_copies = available_copies + 1 WHERE book_id = %s", (book_id,))
                
                conn.commit()
                conn.close()
                print("Book returned successfully!")
            else:
                print("Invalid transaction ID or book already returned.")

    @staticmethod
    def get_all_transactions():
        """Retrieves all transactions from the database"""
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            query = "SELECT * FROM transactions"
            cursor.execute(query)
            transactions = cursor.fetchall()
            conn.close()
            return transactions

# Test the functionality
if __name__ == "__main__":
    Transaction.issue_book(1, 1)  # Issue a book (use existing book_id and member_id)
    transactions = Transaction.get_all_transactions()
    print(transactions)