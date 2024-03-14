from flask import Flask, request
from flask_cors import CORS
import db_access
from book import Book

app = Flask(__name__)
CORS(app)

@app.route('/books', methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        conn = db_access.connect_db('bookstore.db')
        cursor = db_access.get_cursor(conn)
        books = db_access.get_books(cursor)
        books_dict = []
        for book in books:
            books_dict.append(book.__dict__)
        conn.close()
        return books_dict

    elif request.method == 'POST':
        conn = db_access.connect_db('bookstore.db')
        cursor = db_access.get_cursor(conn)
        data = request.get_json()
        book = Book(data['title'], data['author'], data['publisher'])
        db_access.insert_book(cursor, book)
        db_access.commit(conn)
        conn.close()
        return book.__dict__

