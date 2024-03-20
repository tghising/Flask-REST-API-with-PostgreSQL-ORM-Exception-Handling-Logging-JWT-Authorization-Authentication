from app import db
from datetime import datetime


class ResetToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    token = db.Column(db.String(100), unique=True, nullable=False)
    expiration_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, user_id, token, expiration_time):
        self.user_id = user_id
        self.token = token
        self.expiration_time = expiration_time

    def is_expired(self):
        return datetime.utcnow() > self.expiration_time

    def __repr__(self):
        return f"ResetToken('{self.user_id}', '{self.token}', '{self.expiration_time}')"
