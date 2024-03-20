
def initialize_routes(api):
    from app.controllers.book_controller import BookController, BooksController
    from app.controllers.auth.auth_controller import Signup, Login
    from app.controllers.auth.user_controller import ForgotPassword, ResetPassword
    from app.controllers.home import Home

    api.add_resource(Home, '/')

    api.add_resource(Signup, '/api/auth/signup')
    api.add_resource(Login, '/api/auth/login')
    api.add_resource(ForgotPassword, '/api/auth/forgot-password')
    api.add_resource(ResetPassword, '/api/auth/reset-password')

    # Register BookResource to handle '/api/books' and '/api/books/<id>' routes
    api.add_resource(BooksController, '/api/books')
    api.add_resource(BookController, '/api/books/<id>')
