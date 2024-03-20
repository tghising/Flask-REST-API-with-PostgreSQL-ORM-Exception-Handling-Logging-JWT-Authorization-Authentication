from app.models.auth.user import User
from app.utils.jwt_utils import generate_access_token


class AuthService:
    @staticmethod
    def authenticate(identifier, password):
        user = User.query.filter((User.username == identifier) | (User.email == identifier)).first()
        if user and user.verify_password(password):
            return user

    @staticmethod
    def generate_token(user):
        from run import app
        expires = app.config['TOKEN_EXPIRATION_TIME']
        return generate_access_token(user.username, expires)
