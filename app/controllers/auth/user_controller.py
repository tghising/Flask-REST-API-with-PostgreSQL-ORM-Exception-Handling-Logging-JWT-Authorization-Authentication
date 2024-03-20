from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse

from app.exceptions.custom_exceptions import InternalServerError, CustomException
from app.services.auth.reset_token_service import ResetTokenService
from app.services.auth.user_service import UserService
from app.services.mail_service import send_email
from app.utils.jwt_utils import decode_access_token


class ChangePassword(Resource):
    @jwt_required()
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('user_id', type=int, required=True, help="User ID is required")
            parser.add_argument('password', type=str, required=True, help="New password is required")
            data = parser.parse_args()

            current_user = get_jwt_identity()
            if current_user != data['user_id']:
                raise CustomException("You are not authorized to change your password", 403)

            user = UserService.find_user_by_id(data['user_id'])
            if not user:
                raise CustomException("User not found", 404)

            UserService.change_password(user, data['password'])
            return {'message': 'Password changed successfully'}, 200

        except InternalServerError:
            raise InternalServerError


class UpdateProfile(Resource):
    @jwt_required()
    def put(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('new_username', type=str, required=True, help="New username is required")
            parser.add_argument('new_email', type=str, required=True, help="New email is required")
            data = parser.parse_args()

            current_user_id = get_jwt_identity()
            user = UserService.find_user_by_id(current_user_id)
            if not user:
                raise CustomException("User not found", 404)
            UserService.update_profile(user, data['new_username'], data['new_email'])
            return {'message': 'Profile updated successfully'}, 200

        except InternalServerError:
            raise InternalServerError


class ForgotPassword(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str, required=True, help="Email is required")
            data = parser.parse_args()

            user = UserService.find_user_by_email(data['email']).first()
            if not user:
                raise CustomException("User not found", 404)

            reset_token = ResetTokenService.generate_reset_token(user.id)
            host_url = request.host_url

            # Send password reset email
            reset_link = f"{host_url}/reset-password?token={reset_token}"
            return send_email(
                subject='Reset Your Password',
                sender='info@test.com',
                recipients=[user.email],
                text_body=f"Click the following link to reset your password: {reset_link}",
                html_body=f"Click the following link to reset your password: {reset_link}"
            )

        except InternalServerError:
            raise InternalServerError


class ResetPassword(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('token', type=str, required=True, help="Token is required")
            parser.add_argument('new_password', type=str, required=True, help="New password is required")
            data = parser.parse_args()

            reset_token = data['reset_token']
            new_password = data['new_password']

            # Decode the access token
            decoded_token = decode_access_token(reset_token)
            if decoded_token is None or not new_password:
                raise CustomException("Invalid or expired token", 400)

            reset_password = ResetTokenService.reset_password_with_token(token=reset_token, new_password=new_password)
            if not reset_password:
                return {'message': 'Password reset successfully'}, 200
            else:
                raise CustomException("Password reset unsuccessful", 500)

        except Exception as e:
            raise InternalServerError
