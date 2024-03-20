from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.config.config import Server_Configs
from app.routing.routes import initialize_routes
from app.utils.logging_utils import configure_logging, init_log_request_info, init_log_response_info

# Initialize SQL
db = SQLAlchemy()

bcrypt = Bcrypt()
jwt = JWTManager()

# Migrate
migrate = Migrate()

mail = Mail()


def create_app(environment='development'):
    app = Flask(__name__)

    server_config = Server_Configs[environment]

    app.config.from_object(server_config)

    # Configure logging
    configure_logging(server_config)

    # Middleware for request logging
    app.before_request(init_log_request_info)

    # Middleware for response logging
    app.after_request(init_log_response_info)

    db.init_app(app)

    # Migrate
    migrate.init_app(app, db)

    # initialize the api: Main entry point for the application
    api = Api(app)

    bcrypt.init_app(app)
    jwt.init_app(app)

    mail.init_app(app)

    # Initialize routes for the API endpoints
    initialize_routes(api)

    # Global error handler for all custom exceptions
    from app.exceptions.exception_handling import initialize_exception_handling
    initialize_exception_handling(app)

    # TODO Do not remove: Flask does not automatically detect models so, we need to import all models to let the migrate tool know
    from app.models.book import Book
    from app.models.auth.user import User
    from app.models.auth.reset_token import ResetToken

    return app
