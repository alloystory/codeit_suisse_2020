from flask import Blueprint, request
from src.controllers.books import BooksController
from src.models.books import BooksModel

model = BooksModel()
controller = BooksController(model)

router = Blueprint('books_router', __name__)

@router.route('/', methods = ['GET'])
def get_books():
    return controller.get_books()

@router.route('/<int:id>', methods = ['GET'])
def get_book_by_id(id):
    return controller.get_book_by_id(id)

@router.route('/add', methods = ['POST'])
def add_book():
    data = request.get_json()
    return controller.add_book(data)

@router.route('/delete/<int:id>', methods = ['GET'])
def delete_book_by_id(id):
    return controller.delete_book_by_id(id)

@router.route('/edit/<int:id>', methods = ['POST'])
def edit_book_by_id(id):
    data = request.get_json()
    return controller.edit_book_by_id(id, data)