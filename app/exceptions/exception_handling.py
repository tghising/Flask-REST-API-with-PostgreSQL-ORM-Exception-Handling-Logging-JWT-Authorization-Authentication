from flask import jsonify
from app.exceptions.custom_exceptions import CustomException


# Global error handler for all custom exceptions
def initialize_exception_handling(app):
    @app.errorhandler(CustomException)
    def handle_custom_exception(error):
        app.logger.error(str(error))
        response = jsonify({'error': str(error)})
        response.status_code = error.status_code
        return response
