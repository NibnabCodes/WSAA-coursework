# simple flask server

from flask import Flask, request, jsonify  

app = Flask(__name__)

# Simple in-memory "database"
books = [
    {"id": 1, "title": "Brave New World", "author": "Aldous Huxley", "price": 5},
    {"id": 2, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "price": 6}
]

# basic test endpoint to confirm the server works
# http://127.0.0.1:5000/
@app.route('/')
def index():
        return "Book API is running"

# Get all books
# curl http://127.0.0.1:5000/books
@app.route('/books', methods=['GET'])
def getall():
    return jsonify(books)


# Find by id
# curl http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Create Book
# curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"Animal Farm\",\"author\":\"George Orwell\",\"price\":10}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    newbook = request.json

    # create new id
    newbook["id"] = books[-1]["id"] + 1 if books else 1
 
    books.append(newbook)

    return jsonify(newbook), 201

# update book by id - example shows how to update just the price, but you can also update title and author by including them in the JSON body
# curl.exe -X PUT -H "Content-Type: application/json" -d "{\"price\":123}" http://127.0.0.1:5000/books/3

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    updatedbook = request.json

    for book in books:
        if book["id"] == id:
            book["title"] = updatedbook.get("title", book["title"])
            book["author"] = updatedbook.get("author", book["author"])
            book["price"] = updatedbook.get("price", book["price"])

            return jsonify(book)

    return jsonify({"error": "Book not found"}), 404

# Delete Book by id
# curl -X DELETE  http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    for book in books:
        if book["id"] == id:
            books.remove(book)
            return jsonify({"message": "Book deleted"})

    return jsonify({"error": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug = True)