from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

books = []

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    books.append(data)
    return jsonify({"message": "Book added successfully"})

@app.route('/books/<int:index>', methods=['DELETE'])
def delete_book(index):
    del books[index]
    return jsonify({"message": "Book deleted successfully"})

@app.route('/books/<int:index>', methods=['PUT'])
def update_book(index):
    data = request.get_json()
    books[index] = data
    return jsonify({"message": "Book updated successfully"})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000" ,debug=True)
