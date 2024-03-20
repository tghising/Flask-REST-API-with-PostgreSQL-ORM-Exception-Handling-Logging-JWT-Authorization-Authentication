import secrets

from app import db
from datetime import datetime

from app.models.auth.reset_token import ResetToken
from app.services.auth.user_service import UserService


class ResetTokenService:
    @staticmethod
    def generate_reset_token(user_id):
        from run import app
        token = secrets.token_urlsafe(32)
        expiration_time = datetime.utcnow() + app.config['RESET_TOKEN_EXPIRATION']
        reset_token = ResetToken(user_id=user_id, token=token, expiration_time=expiration_time)
        db.session.add(reset_token)
        db.session.commit()
        return token

    @staticmethod
    def reset_password_with_token(token, new_password):
        """Reset user's password using the provided reset token."""
        reset_token = ResetTokenService.get_reset_token_by_token(token=token)

        if reset_token and not reset_token.is_expired():
            user = UserService.find_user_by_id(reset_token.user_id)
            if user:
                UserService.reset_password(user, new_password)
                ResetTokenService.delete_reset_token(reset_token)
                return True
        return False

    @staticmethod
    def get_reset_token_by_token(token):
        """Retrieve a reset token by its token value."""
        return ResetToken.query.filter_by(token=token).first()

    @staticmethod
    def delete_reset_token(reset_token):
        """Delete a reset token."""
        db.session.delete(reset_token)
        db.session.commit()

    @staticmethod
    def delete_expired_reset_tokens():
        """Delete expired reset tokens."""
        expired_tokens = ResetToken.query.filter(ResetToken.expiration_time < datetime.utcnow()).all()
        for token in expired_tokens:
            db.session.delete(token)

        db.session.commit()

    @staticmethod
    def is_valid_reset_token(token):
        """Check if a reset token is valid (exists and not expired)."""
        reset_token = ResetTokenService.get_reset_token_by_token(token)
        return reset_token and not reset_token.is_expired()
