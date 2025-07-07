from bottle import Bottle, request
from .base_controller import BaseController
from services.user_service import UserService

class UserController(BaseController):
    def __init__(self, app):
        super().__init__(app)

        self.setup_routes()
        self.user_service = UserService()


    # Rotas User
    def setup_routes(self):
        self.app.route('/users', method='GET', callback=self.list_users)
        self.app.route('/users/add', method=['GET', 'POST'], callback=self.add_user)
        self.app.route('/users/edit/<user_id:int>', method=['GET', 'POST'], callback=self.edit_user)
        self.app.route('/users/delete/<user_id:int>', method='POST', callback=self.delete_user)
        self.app.route('/users/<user_id:int>/book', method=['GET, POST'], callback=self)


    def list_users(self):
        users = self.user_service.get_all()
        # Atualiza a contagem para cada usuário
        updated_users = []
        for user in users:
            updated_users.append(
                self.user_service.get_user_with_updated_books(user.id) or user
            )
        return self.render('users', users=updated_users)


    def add_user(self):
        if request.method == 'GET':
            return self.render('user_form', user=None, action="/users/add")
        else:
            # POST - salvar usuário
            self.user_service.save()
            self.redirect('/users')


    def edit_user(self, user_id):
        user = self.user_service.get_by_id(user_id)
        if not user:
            return "Usuário não encontrado"

        if request.method == 'GET':
            return self.render('user_form', user=user, action=f"/users/edit/{user_id}")
        else:
            # POST - salvar edição
            self.user_service.edit_user(user)
            self.redirect('/users')


    # Ainda em teste ----- lista de livros para cada usuário
    def enter_user(self, user_name):
        user = self.user_service.get_user_name(user_name)
        if not user:
            return "Usuário não encontrado"
        
        if request.method == 'GET':
            return self.render('user_list')


    def delete_user(self, user_id):
        self.user_service.delete_user(user_id)
        self.redirect('/users')

    def add_book(self, user_id):
        user = self.user_service.get_by_id(user_id)
        if not user:
            return "Usuário não encontrado"

        if request.method == 'GET':
            return self.render('livros', user=user, action=f"/users/{user_id}/book")
        else:
            # POST - salvar edição
            self.user_service.edit_user(user)
            self.user_service.edit_user_books_add(user)
            self.list_users()
            self.redirect('/users')


user_routes = Bottle()
user_controller = UserController(user_routes)
