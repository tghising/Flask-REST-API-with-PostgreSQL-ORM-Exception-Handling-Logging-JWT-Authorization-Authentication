from app import db
from app.models.auth.user import User


class UserService:
    @staticmethod
    def create_user(username, email, password):
        if not User.query.filter((User.username == username) | (User.email == email)).first():
            try:
                new_user = User(username=username, email=email, password=password)
                new_user.set_password(password)  # Set the password using appropriate hashing method
                db.session.add(new_user)
                db.session.commit()
                return new_user
            except Exception as e:
                # If an error occurs during user creation, rollback the transaction
                db.session.rollback()
                print(f"Error creating user: {e}")
                return None
        else:
            return None

    @staticmethod
    def change_password(user, new_password):
        user.password = new_password
        db.session.commit()

    @staticmethod
    def update_profile(user, new_username, new_email):
        user.username = new_username
        user.email = new_email
        db.session.commit()

    @staticmethod
    def find_user_by_id(user_id):
        """Find a user by their user ID."""
        return User.query.get(id=user_id)

    @staticmethod
    def find_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def find_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def reset_password(user, new_password):
        user.password = new_password
        user.reset_token = None  # Clear the reset token after password reset
        db.session.commit()
