from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# User Mixin for credentials checking
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    shorts = db.relationship('Shorts', backref="user")

    def __repr__(self) -> str:
        return 'User: {self.username}'

class Shorts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app = db.Column(db.String(30), nullable=False)
    target = db.Column(db.String(10), nullable=False)
    original_url = db.Column(db.Text, nullable=False)
    short_name = db.Column(db.String(3), nullable=False)
    last_visit = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return 'Shorts: {self.url}'
