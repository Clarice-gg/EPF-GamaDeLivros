import json
import os
from dataclasses import dataclass, asdict
from typing import List
from models.relationship import delete_relationship

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class User:
    def __init__(self, id, name, email, birthdate, books):
        self.id = id
        self.name = name
        self.email = email
        self.birthdate = birthdate
        self.books = books


    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', email='{self.email}', "
                f"birthdate='{self.birthdate}', books='{self.books}'")


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birthdate': self.birthdate,
            'books': self.books
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            birthdate=data['birthdate'],
            books=data['books']
        )


class UserModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()


    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User(**item) for item in data]


    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)


    def get_all(self):
        return self.users


    def get_by_id(self, user_id: int):
        return next((u for u in self.users if u.id == user_id), None)


    def add_user(self, user: User):
        self.users.append(user)
        self._save()


    def update_user(self, updated_user: User):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break


    def delete_user(self, user_id: int):
        self.users = [u for u in self.users if u.id != user_id]
        delete_relationship(user_id)
        self._save()

    def get_user_name(self, user_name: str):
        return next((u for u in self.users if u.name == user_name), None)


    def update_user_books(self, updated_user):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                updated_user.books += 1
                self.users[i] = updated_user
                self._save()
                break
    
def carregar_users():
    with open('data/users.json') as f:
        return json.load(f)
    