import jwt
from flask import request, abort
from flask_restx import Resource, Namespace

from constants import JWT_SECRET, JWT_ALGORITHM
from dao.model.user import UserSchema
from decorators import auth_required
from implemented import user_service

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        user_data = request.headers['Authorization']
        token = user_data.split('Bearer ')[-1]
        decoded_data = jwt.decode(token, secret=JWT_SECRET, algorithms=JWT_ALGORITHM)
        email = decoded_data.get('email')
        if email:
            return user_schema.dump(user_service.get_user_by_email(email)), 200
        abort(404)

    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "user created", 201

    def patch(self):
        data = request.json
        password = data.get('password')
        if password:
            return "try again", 403

        user_data = request.headers['Authorization']
        token = user_data.split('Bearer ')[-1]
        decode_data = jwt.decode(token, secret=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = decode_data.get('email')
        data['email'] = email

        user = user_service.update(data)
        if not user:
            return abort(404)
        return user_schema.dump(user)


@user_ns.route('/password/')
class UserView(Resource):
    @auth_required
    def put(self):
        data = request.json
        user_data = request.headers['Authorization']
        token = user_data.split('Bearer ')[-1]
        decode_data = jwt.decode(token, secret=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = decode_data.get('email')
        data['email'] = email

        user = user_service.update(data)
        if not user:
            return abort(404)
        return user_schema.dump(user)
