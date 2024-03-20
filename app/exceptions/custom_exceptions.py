class CustomException(Exception):
    def __init__(self, message, status_code):
        super().__init__(message)
        self.status_code = status_code


class InternalServerError(CustomException):
    def __init__(self, message="Something went wrong"):
        super().__init__(message, status_code=500)


class SchemaValidationError(CustomException):
    def __init__(self, message="Request is missing required fields"):
        super().__init__(message, status_code=400)


class BookAlreadyExistsError(CustomException):
    def __init__(self, message="Book with given title already exists"):
        super().__init__(message, status_code=400)


class InvalidOrExpiredTokenError(CustomException):
    def __init__(self, message="Invalid or expired token"):
        super().__init__(message, status_code=400)


class UpdatingBookError(CustomException):
    def __init__(self, message="Updating book added by other is forbidden"):
        super().__init__(message, status_code=403)


class DeletingBookError(CustomException):
    def __init__(self, message="Deleting book added by other is forbidden"):
        super().__init__(message, status_code=403)


class BookNotExistsError(CustomException):
    def __init__(self, message="Book with given id doesn't exists"):
        super().__init__(message, status_code=400)


class EmailAlreadyExistsError(CustomException):
    def __init__(self, message="User with given email address already exists"):
        super().__init__(message, status_code=400)


class UserUsernameEmailAlreadyExistsError(CustomException):
    def __init__(self, message="User with given username, email address already exists"):
        super().__init__(message, status_code=400)


class InvalidCredentialsError(CustomException):
    def __init__(self, message="Invalid username or password"):
        super().__init__(message, status_code=401)
