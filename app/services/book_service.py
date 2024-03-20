from app import db
from app.models.book import Book


class BookService:
    @staticmethod
    def create_book(title, author, year):
        new_book = Book(title=title, author=author, year=year)
        db.session.add(new_book)
        db.session.commit()
        return new_book

    @staticmethod
    def get_book(id):
        return Book.query.get(id)

    @staticmethod
    def get_all_books():
        return Book.query.all()

    @staticmethod
    def update_book(id, title=None, author=None, year=None):
        book = Book.query.get(id)
        if not book:
            return None

        if title:
            book.title = title
        if author:
            book.author = author
        if year:
            book.year = year

        db.session.commit()
        return book

    @staticmethod
    def delete_book(id):
        book = Book.query.get(id)
        if not book:
            return None

        db.session.delete(book)
        db.session.commit()
        return book
