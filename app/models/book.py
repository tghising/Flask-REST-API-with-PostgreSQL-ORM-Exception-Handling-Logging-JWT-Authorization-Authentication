from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    author = db.Column(db.String(128), nullable=False)
    year = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'<Book {self.title} by {self.author}>'

    