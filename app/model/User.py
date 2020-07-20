from app import db
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):

    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True, unique=True)
    email = Column(String(128), index=True, unique=True)
    password_hash = Column(String(128))

    def __repr__(self):
        return "Name: {}, Email: {}".format(self.username, self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
