from flask_restx import Resource, Namespace
from flask import request

from dao.model.movie import MovieSchema
from implemented import movie_service
from decorators import auth_required

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        try:
            status = request.args.get('status')
            page = request.args.get('page')

            filters = {
                "status": status,
                "page": page,

            }
            movie = movie_service.get_all(filters)
            return movies_schema.dump(movie), 200
        except Exception as e:
            return 404


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid: int):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return "movie not found"
