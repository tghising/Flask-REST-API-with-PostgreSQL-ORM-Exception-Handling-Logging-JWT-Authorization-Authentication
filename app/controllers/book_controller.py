from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

from app.exceptions.custom_exceptions import CustomException, InternalServerError
from app.services.book_service import BookService

book_service = BookService()


class BooksController(Resource):
    @jwt_required()
    def get(self):
        try:
            books = book_service.get_all_books()
            if not books:
                raise CustomException("No books found", 404)

            return [{'id': book.id, 'title': book.title, 'year': book.year, 'author': book.author} for book in books], 200

        except InternalServerError:
            raise InternalServerError

    @jwt_required()
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, required=True, help='Title is required')
            parser.add_argument('author', type=str, required=True, help='Author is required')
            parser.add_argument('year', type=int)
            data = parser.parse_args()

            title = data['title']
            author = data['author']
            year = data['year']

            if not title or not author:
                raise CustomException("Title and author are required", 400)

            new_book = book_service.create_book(title, author, year)
            return {'id': new_book.id, 'title': new_book.title, 'year': new_book.year, 'author': new_book.author}, 201

        except InternalServerError:
            raise InternalServerError


class BookController(Resource):
    @jwt_required()
    def get(self, id=None):
        try:
            book = book_service.get_book(id)
            if not book:
                raise CustomException("Book not found", 404)

            return {'id': book.id, 'title': book.title, 'year': book.year, 'author': book.author}, 200

        except InternalServerError:
            raise InternalServerError

    @jwt_required()
    def put(self, id):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str)
            parser.add_argument('author', type=str)
            parser.add_argument('year', type=int)
            args = parser.parse_args()

            title = args.get('title')
            author = args.get('author')
            year = args.get('year')

            updated_book = book_service.update_book(id, title, author, year)
            if not updated_book:
                raise CustomException("Book not found", 404)

            return {'id': updated_book.id, 'title': updated_book.title, 'year': updated_book.year, 'author': updated_book.author}, 200
        except InternalServerError:
            raise InternalServerError

    @jwt_required()
    def delete(self, id):
        try:
            deleted_book = book_service.delete_book(id)
            if not deleted_book:
                raise CustomException("Book not found", 404)

            return {'id': deleted_book.id, 'title': deleted_book.title, 'year': deleted_book.year, 'author': deleted_book.author}, 200
        except InternalServerError:
            raise InternalServerError
