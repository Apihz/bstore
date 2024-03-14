import sqlite3

from book import Book

def connect_db(name_of_db):
    conn = sqlite3.connect(name_of_db)
    return conn

def get_cursor(conn):
    return conn.cursor()

def get_books(cursor):
    cursor.execute('SELECT title,author,publisher FROM books')
    rows = cursor.fetchall()
    books=[]
    for row in rows :
        book = Book(row[0], row[1], row[2])
        books.append(book)
    return books

def get_book(cursor, title):
    cursor.execute('SELECT title,author,publisher FROM books WHERE title=?'(title))
    row =  cursor.fetchone()
    if row is None:
            return None
    else: 
        return Book(row[0], row[1], row[2])

def insert_book(cursor, book:Book):
    cursor.execute('INSERT INTO books (title,author,publisher) VALUES (?,?,?)',(book.title, book.author, book.publisher))

def commit(conn):
    conn.commit()