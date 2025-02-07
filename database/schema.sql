-- Create database (if not exists)
CREATE DATABASE IF NOT EXISTS
library_management;
USE library_management;

-- Table for storing book details
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    total_copies INT NOT NULL,
    available_copies INT NOT NULL,
    added_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing member details
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(15),
    joined_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for stroing transactions (book issue/return)
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    issue_date DATE NOT NULL,
    return_date DATE,
    status ENUM('issued', 'returned') DEFAULT 'issued',
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);