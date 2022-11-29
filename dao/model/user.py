from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String)
    user_surname = db.Column(db.String)
    favorite_genre = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False, unique=True)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    user_surname = fields.Str()
    favorite_genre = fields.Str()
    email = fields.Str()
    password = fields.Str()
