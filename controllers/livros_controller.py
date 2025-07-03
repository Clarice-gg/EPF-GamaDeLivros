from bottle import Bottle, request
from .base_controller import BaseController
from services.livros_service import LivroService

class LivroController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.book_service = LivroService()


    # Rotas Livros
    def setup_routes(self):
        self.app.route('/books', method='GET', callback=self.list_books)
        self.app.route('/books/add', method=['GET', 'POST'], callback=self.add_book)
        self.app.route('/books/edit/<book_id:int>', method=['GET', 'POST'], callback=self.edit_book)
        self.app.route('/books/delete/<book_id:int>', method='POST', callback=self.delete_book)


    def list_books(self):
        books = self.book_service.get_all()
        return self.render('book', books=books)


    def add_book(self):
        if request.method == 'GET':
            return self.render('book_form', book=None, action="/books/add")
        else:
            # POST - salvar livro
            self.book_service.save()
            self.redirect('/books')


    def edit_book(self, book_id):
        book = self.book_service.get_by_id(book_id)
        if not book:
            return "Livro não encontrado"

        if request.method == 'GET':
            return self.render('book_form', book=book, action=f"/books/edit/{book_id}")
        else:
            # POST - salvar edição
            self.book_service.edit_book(book)
            self.redirect('/books')


    def delete_book(self, book_id):
        self.book_service.delete_book(book_id)
        self.redirect('/books')


book_routes = Bottle()
book_controller = LivroController(book_routes)