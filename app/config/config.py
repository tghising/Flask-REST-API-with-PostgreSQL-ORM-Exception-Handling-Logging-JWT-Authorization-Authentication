import logging
from datetime import timedelta

DATABASE_CONFIG = {
    'username': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': '5432',
    'database': 'test-db'
}


class Config:
    # TODO need to config from yml or env file
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'your_secret_key_here'
    JWT_SECRET_KEY = 'your_jwt_secret_key_here'
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Token expiration time in seconds

    # Define reset token expiration time
    RESET_TOKEN_EXPIRATION = timedelta(hours=1)  # Reset token expires in 1 hour
    TOKEN_EXPIRATION_TIME = timedelta(hours=1)  # token expires in 1 hour
    REFRESH_TOKEN_EXPIRATION_TIME = timedelta(hours=1)  # refresh token expires in 1 hour
    TOKEN_EXPIRATION_DELTA = timedelta(hours=1)  # token expires in 1 hour

    # Flask-Mail settings
    MAIL_SERVER = 'localhost'  # Specify your SMTP server
    MAIL_PORT = 1025  # Specify the port
    MAIL_USE_TLS = True  # Enable TLS encryption
    MAIL_USERNAME = 'admin@test.com'  # Your email address
    MAIL_PASSWORD = ''  # Your email password

    LOGGING_LEVEL = logging.INFO
    DB_LOGGING_LEVEL = logging.INFO
    APP_LOG_FILE_PATH = 'logs/app.log'
    DB_LOG_FILE_PATH = 'logs/db.log'


class DevConfig(Config):
    # TODO need to config from yml or env file
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'your_secret_key_here'
    JWT_SECRET_KEY = 'your_jwt_secret_key_here'
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Token expiration time in seconds

    # Define reset token expiration time
    RESET_TOKEN_EXPIRATION = timedelta(hours=1)  # Reset token expires in 1 hour
    TOKEN_EXPIRATION_TIME = timedelta(minutes=1)  # token expires in 1 hour
    REFRESH_TOKEN_EXPIRATION_TIME = timedelta(hours=1)  # refresh token expires in 1 hour
    TOKEN_EXPIRATION_DELTA = timedelta(hours=1)  # token expires in 1 hour

    # Flask-Mail settings
    MAIL_SERVER = 'localhost'  # Specify your SMTP server
    MAIL_PORT = 1025  # Specify the port
    MAIL_USE_TLS = True  # Enable TLS encryption
    MAIL_USERNAME = 'admin@test.com'  # Your email address
    MAIL_PASSWORD = ''  # Your email password

    LOGGING_LEVEL = logging.DEBUG
    DB_LOGGING_LEVEL = logging.DEBUG
    APP_LOG_FILE_PATH = 'logs/app.log'
    DB_LOG_FILE_PATH = 'logs/db.log'

    # SQLALCHEMY_ECHO = True
    DEBUG = True


class TestConfig(Config):
    # TODO need to config from yml or env file
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    SECRET_KEY = 'your_secret_key_here'
    JWT_SECRET_KEY = 'your_jwt_secret_key_here'
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Token expiration time in seconds

    # Define reset token expiration time
    RESET_TOKEN_EXPIRATION = timedelta(hours=1)  # Reset token expires in 1 hour
    TOKEN_EXPIRATION_TIME = timedelta(hours=1)  # token expires in 1 hour
    REFRESH_TOKEN_EXPIRATION_TIME = timedelta(hours=1)  # refresh token expires in 1 hour
    TOKEN_EXPIRATION_DELTA = timedelta(hours=1)  # token expires in 1 hour

    # Flask-Mail settings
    MAIL_SERVER = 'localhost'  # Specify your SMTP server
    MAIL_PORT = 1025  # Specify the port
    MAIL_USE_TLS = True  # Enable TLS encryption
    MAIL_USERNAME = 'admin@objectdetection.com'  # Your email address
    MAIL_PASSWORD = ''  # Your email password

    LOGGING_LEVEL = logging.INFO
    DB_LOGGING_LEVEL = logging.INFO
    APP_LOG_FILE_PATH = 'logs/app.log'
    DB_LOG_FILE_PATH = 'logs/db.log'


class ProdConfig(Config):
    # TODO need to config from yml or env file
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    SECRET_KEY = 'your_secret_key_here'
    JWT_SECRET_KEY = 'your_jwt_secret_key_here'
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Token expiration time in seconds

    # Define reset token expiration time
    RESET_TOKEN_EXPIRATION = timedelta(hours=1)  # Reset token expires in 1 hour
    TOKEN_EXPIRATION_TIME = timedelta(hours=1)  # token expires in 1 hour
    REFRESH_TOKEN_EXPIRATION_TIME = timedelta(hours=1)  # refresh token expires in 1 hour
    TOKEN_EXPIRATION_DELTA = timedelta(hours=1)  # token expires in 1 hour

    # Flask-Mail settings
    MAIL_SERVER = 'localhost'  # Specify your SMTP server
    MAIL_PORT = 1025  # Specify the port
    MAIL_USE_TLS = True  # Enable TLS encryption
    MAIL_USERNAME = 'admin@objectdetection.com'  # Your email address
    MAIL_PASSWORD = ''  # Your email password

    LOGGING_LEVEL = logging.INFO
    DB_LOGGING_LEVEL = logging.INFO
    APP_LOG_FILE_PATH = 'logs/app.log'
    DB_LOG_FILE_PATH = 'logs/db.log'

    DEBUG = True


Server_Configs = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
}
