# This file is managed by Student 2
from database.db_connection import get_db_connection

class Member:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        
    @staticmethod
    def add_member(name, email, phone):
        """Adds a new member to the database"""
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO members (name, email, phone) VALUES (%s, %s, %s)"
            values = (name, email, phone)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            print("Member added successfully!")
            
    @staticmethod
    def update_member(member_id, name=None, email=None, phone=None):
        """Updates member details in the database"""
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            updates = []
            values = []
            
            if name:
                updates.append("name = %s")
                values.append(name)
            if email:
                updates.append("email = %s")
                values.append(email)
            if phone:
                updates.append("phone = %s")
                values.append(phone)
                
            if updates:
                query = f"UPDATE members SET {', '.join(updates)} WHERE member_id = %s"
                values.append(member_id)
                cursor.execute(query, values)
                conn.commit()
                
            conn.close()
            print("Member updated successfully!")
            
    @staticmethod
    def delete_member (member_id):
        """Deletes a member from the database"""
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            query = "DELETE FROM members WHERE member_id = %s"
            cursor.execute(query, (member_id,))
            conn.commit()
            conn.close()
            print("Member deleted successfully!")
            
    @staticmethod
    def get_all_members():
        """Retrieves all members from the database"""
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            query = "SELECT * FROM members"
            cursor.execute(query)
            members = cursor.fetchall()
            conn.close()
            return members
        
    # Test the functionality
    if __name__ == "__main__":
        Member.add_member("Alice Johnson","alice@example.com","9876543210")
        members = Member.get_all_members()
        print(members)
        