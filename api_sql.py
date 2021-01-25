import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

def connection():
    conn = sqlite3.connect('books.db')
    return conn


@app.route('/create/book/store')
def bookstore():
    # cre_t_query = "CREATE TABLE book_db (id INTEGER, title VARCHAR, author VARCHAR, first_sentence VARCHAR, year_published VARCHAR);"
    cur = connection()
    # res = cur.execute(cre_t_query).fetchall()
    for book in books:
        ins_q = 'INSERT INTO book_db (id,title,author,first_sentence,year_published) VALUES ({id}, "{title}","{author}", "{first_sentence}", "{year_published}")'.format(
            id = book.get('id'), title=book.get('title'), author=book.get('author'),
            first_sentence=book.get('first_sentence'), year_published=book.get('year_published')
        )
        res = cur.execute(ins_q).fetchall()
        print(res)
    return jsonify("Success")

@app.route('/api/all_books', methods=['GET'])
def getAllBooks():
    cur = connection()
    res = cur.execute("SELECT * FROM book_db WHERE id = 0;").fetchall()
    print(res)
    return jsonify(res)

@app.route('/api/book/get', methods=['GET'])
def get_rqr_book():
    book_id = None
    if 'id' in request.args:
        book_id = int(request.args['id'])
    for book in books:
        if book.get('id') == book_id:
            return jsonify(book)
    else:
        return jsonify("Book Not Found")

app.run(port=4325)