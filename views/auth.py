from flask_restx import Resource, Namespace
from flask import request, abort
from implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthView(Resource):
    def post(self):
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)
        if email is None or password is None:
            return "отсутствуют логин или пароль", 400

        user_service.create(data)

        return '', 201


@auth_ns.route('/login/')
class AuthView(Resource):
    def post(self):
        data = request.json
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None or password is None:
            return '', 400
        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        try:
            data = request.json
            refresh_token = data.get("refresh_token")
            tokens = auth_service.approve_refresh_token(refresh_token)

            return tokens, 201

        except Exception as e:
            abort(400)
