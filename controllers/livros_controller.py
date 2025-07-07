from bottle import Bottle, request, template
from .base_controller import BaseController
from services.livros_service import LivroService
from services.relationship import (registrar_escolha_livro, remover_livro_usuario, livros_do_usuario)
from models.livros import carregar_livros
from models.user import UserModel
from services.user_service import UserService
from controllers.user_controller import UserController


class LivroController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.book_service = LivroService()
        self.user_service = UserService()
        self.user_controller = UserController(app)


    # Rotas Livros
    def setup_routes(self):
        self.app.route('/books', method='GET', callback=self.list_books)
        self.app.route('/books/add', method=['GET', 'POST'], callback=self.add_book)
        self.app.route('/books/edit/<book_id:int>', method=['GET', 'POST'], callback=self.edit_book)
        self.app.route('/books/delete/<book_id:int>', method='POST', callback=self.delete_book)
        self.app.route('/users/<user_id:int>/books', method='GET', callback=self.mostrar_livros)
        self.app.route('/users/<user_id:int>/books/<book_id:int>/escolher', method='POST', callback=self.escolher_livro)
        self.app.route('/users/<user_id:int>/books/<book_id:int>/remover', method='POST', callback=self.remover_livro)


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

    
    def mostrar_livros(self, user_id):
        books = carregar_livros()
        ids_escolhidos = livros_do_usuario(user_id)
        livros_escolhidos = [b for b in books if b['id'] in ids_escolhidos]
        livros_disponiveis = [b for b in books if b['id'] not in ids_escolhidos]

    # Tá dando erro aqui -------- revisar ---------
        return self.render('livros.tpl',
                        user_id = user_id,
                        livros_escolhidos = livros_escolhidos,
                        livros_disponiveis = livros_disponiveis,
                        action=f"/users/{user_id}/books")


    def escolher_livro(self, user_id, book_id):
        registrar_escolha_livro(user_id, book_id)
        #user = self.user_service.get_by_id(user_id)
        self.user_service.add_book_to_user(user_id, book_id)
        self.redirect(f'/users/{user_id}/books')
        self.user_controller.list_users()

    def remover_livro(self, user_id, book_id):
        remover_livro_usuario(user_id, book_id)
        #user = self.user_service.get_by_id(user_id)
        self.user_service.remove_book_from_user(user_id, book_id)
        self. redirect(f'/users/{user_id}/books')
        self.user_controller.list_users()


book_routes = Bottle()
book_controller = LivroController(book_routes)