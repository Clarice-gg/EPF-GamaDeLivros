import json
import os

arquivo = 'data/relationship.json'

def carregar_relacionamentos():
    if not os.path.exists(arquivo):
        return []
    with open(arquivo) as f:
        data = json.load(f)
        return data
        

def salvar_relacionamentos(relacionamentos):
    with open(arquivo, 'w') as f:
        json.dump(relacionamentos, f, indent=2)


def registrar_escolha_livro(user_id, book_id):
    dados = carregar_relacionamentos()
    if any(r['user_id'] == user_id and r['book_id'] == book_id for r in dados):
        return
    
    dados.append({'user_id': user_id, 'book_id': book_id})
    salvar_relacionamentos(dados)


def remover_livro_usuario(user_id, book_id):
    dados = carregar_relacionamentos()
    dados = [r for r in dados if not (r['user_id'] == user_id and r['book_id'] == book_id)]
    salvar_relacionamentos(dados)


def livros_do_usuario(user_id):
    return [r['book_id'] for r in carregar_relacionamentos() if r['user_id'] == user_id]


def usuarios_do_livro(book_id):
    return [r['user_id'] for r in carregar_relacionamentos() if r['book_id'] == book_id]
