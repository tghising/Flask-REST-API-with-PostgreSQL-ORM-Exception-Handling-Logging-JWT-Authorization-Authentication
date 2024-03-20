from flask_restful import Resource, reqparse

from app.exceptions.custom_exceptions import InternalServerError, CustomException
from app.services.auth.auth_service import AuthService
from app.services.auth.user_service import UserService


class Login(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            # parser.add_argument('identifier', type=str, required=True, help="Username or email is required")
            parser.add_argument('username', type=str, required=True, help="Username is required")
            parser.add_argument('password', type=str, required=True, help="Password is required")
            data = parser.parse_args()

            user = AuthService.authenticate(data['identifier'], data['password'])
            if not user:
                raise CustomException("Invalid credentials", 401)

            token = AuthService.generate_token(user)
            return {'token': token}, 200

        except Exception as e:
            raise InternalServerError


class Signup(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, required=True, help="Username is required")
            parser.add_argument('email', type=str, required=True, help="Email is required")
            parser.add_argument('password', type=str, required=True, help="Password is required")
            data = parser.parse_args()

            user = UserService.create_user(data['username'], data['email'], data['password'])
            if not user:
                raise CustomException("User with given username, email address already exists", 400)

            return {'message': 'User created successfully'}, 201

        except InternalServerError:
            raise InternalServerError
