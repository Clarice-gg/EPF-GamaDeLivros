from bottle import Bottle
from controllers.user_controller import user_routes
from controllers.livros_controller import book_routes

def init_controllers(app: Bottle):
    app.merge(user_routes)
    app.merge(book_routes)