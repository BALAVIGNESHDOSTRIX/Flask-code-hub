import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config['DEBUG'] = True

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

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/all_books', methods=['GET'])
def getAllBooks():
    return jsonify(books)

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



app.run(port=6378)