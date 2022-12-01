from flask_restx import Resource, Namespace
from flask import request

from dao.model.director import DirectorSchema
from implemented import director_service

from decorators import auth_required

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):

        try:
            director = director_service.get_all()
            return directors_schema.dump(director), 200
        except Exception as e:
            return 404


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did: int):
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception as e:
            return "director not found"
