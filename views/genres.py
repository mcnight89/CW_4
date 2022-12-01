from flask_restx import Resource, Namespace
from flask import request

from dao.model.genre import GenreSchema
from implemented import genre_service

from decorators import auth_required

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):

        try:
            genre = genre_service.get_all()
            return genres_schema.dump(genre), 200
        except Exception as e:
            return 404


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid: int):
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception as e:
            return "genre not found"
