from bottle import request
from models.user import UserModel, User
from models.relationship import livros_do_usuario, registrar_escolha_livro,remover_livro_usuario


class UserService:
    def __init__(self):
        self.user_model = UserModel()


    def get_all(self):
        users = self.user_model.get_all()
        return users


    def save(self):
        last_id = max([u.id for u in self.user_model.get_all()], default=0)
        new_id = last_id + 1
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')

        user = User(id=new_id, name=name, email=email, birthdate=birthdate, books=0)
        self.user_model.add_user(user)
        self._sync_user_books(new_id)


    def get_by_id(self, user_id):
        return self.user_model.get_by_id(user_id)

    def get_user_name(self, user_name):
        return self.user_model.get_user_name(user_name)

    def edit_user(self, user):
        name = request.forms.get('name')
        email = request.forms.get('email')
        birthdate = request.forms.get('birthdate')

        user.name = name
        user.email = email
        user.birthdate = birthdate

        self.user_model.update_user(user)


    def delete_user(self, user_id):
        self.user_model.delete_user(user_id)

    
    def edit_user_books_add(self, user):
        user.books += 1
        self.user_model.update_user(user)

    def edit_user_books_remove(self, user):
        user.books -= 1
        self.user_model.update_user(user)

    def _sync_user_books(self, user_id: int):
        user = self.user_model.get_by_id(user_id)
        if user:
            user.books = len(livros_do_usuario(user_id))
            self.user_model.update_user(user)
    
    def add_book_to_user(self, user_id: int, book_id: int):
        registrar_escolha_livro(user_id, book_id)
        self._sync_user_books(user_id)
    
    def remove_book_from_user(self, user_id: int, book_id: int):
        remover_livro_usuario(user_id, book_id)
        self._sync_user_books(user_id)
    
    def get_user_with_updated_books(self, user_id):
        user = self.get_by_id(user_id)
        if user:
            self._sync_user_books(user_id)
            return self.get_by_id(user_id) 
        return None
