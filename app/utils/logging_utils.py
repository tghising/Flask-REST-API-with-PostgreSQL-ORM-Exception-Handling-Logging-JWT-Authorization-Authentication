import logging
import os
from logging.handlers import RotatingFileHandler
from flask import request

from app.config.config import Config


class ProductionFilter(logging.Filter):
    def filter(self, record):
        # Check if the application is running in the production environment
        return 'production' in record.getMessage()


def configure_logging(server_config: Config):
    # Configure console logging
    logging.basicConfig(level=server_config.LOGGING_LEVEL, format='[%(asctime)s] [%(levelname)s] [%(name)s] [%(module)s:%(funcName)s] - %(message)s')

    # Create a logger for app
    app_logger = logging.getLogger(__name__)
    app_logger.setLevel(server_config.LOGGING_LEVEL)

    app_log_directory = os.path.dirname(server_config.APP_LOG_FILE_PATH)

    # Create the directory if it doesn't exist
    os.makedirs(app_log_directory, exist_ok=True)

    # Configure file handler for logging
    file_handler = RotatingFileHandler(server_config.APP_LOG_FILE_PATH, maxBytes=1024 * 1024, backupCount=5)
    file_handler.setLevel(server_config.LOGGING_LEVEL)
    # Apply the filter to the file handler
    # file_handler.addFilter(ProductionFilter())
    file_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] [%(module)s:%(funcName)s] - %(message)s'))
    app_logger.addHandler(file_handler)

    # Create and configure a logger for database-related logging
    db_logger = logging.getLogger(__name__)
    db_logger.setLevel(server_config.DB_LOGGING_LEVEL)

    db_log_directory = os.path.dirname(server_config.DB_LOG_FILE_PATH)

    # Create the directory if it doesn't exist
    os.makedirs(db_log_directory, exist_ok=True)

    # Configure file handler for logging
    db_file_handler = RotatingFileHandler(server_config.DB_LOG_FILE_PATH, maxBytes=1024 * 1024, backupCount=5)
    db_file_handler.setLevel(server_config.DB_LOGGING_LEVEL)
    # Apply the filter to the file handler
    # db_file_handler.addFilter(ProductionFilter())
    db_file_handler.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] [%(module)s:%(funcName)s] - %(message)s'))
    db_logger.addHandler(file_handler)


def init_log_request_info():
    logger = logging.getLogger(__name__)
    logger.info("Request: %s %s", request.method, request.url)


def init_log_response_info(response):
    logger = logging.getLogger(__name__)
    logger.info("Response: %s", response.status_code)
    return response
