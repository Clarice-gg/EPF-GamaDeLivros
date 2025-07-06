import json
import os
from typing import List
from user import User
from livros import Livro

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Adm(User):
    def __init__(self, name, email, birthdate, senha):
        super(name, email, birthdate)
        self.senha = senha


class AdmModel:
    FILE_PATH = os.path.join(DATA_DIR, 'list.json')

    def __init__(self):
        self.users = self._load()


    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User(**item) for item in data]



    def mostrar_lista(self, users: User):
        for u in users:
            print(users.name)


    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)
        # indent --> dá 4 espaços;  ensure_ascii=False--> deixa os caracteres como são;  f--> o arquivo para o qual salva
        # u.to_dict --> compreensão de lista, retorna um dicionário

    def get_all(self):
        return self.users


    def get_by_id(self, user_id: int):
        return next((u for u in self.users if u.id == user_id), None)


    def add_list(self, user: User, book: Livro):
        self.users.append(book)
        self._save()


    def update_user(self, updated_user: User):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break


    def delete_list(self, user_id: int):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()

    def get_user_name(self, user_name: str):
        return next((u for u in self.users if u.name == user_name), None)