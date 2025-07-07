# Projeto Template: POO com Python + Bottle + JSON

Este projeto é um sistema de biblioteca virtual, onde é possível o funcionário cadastrar  e retirar livros do "estoque", e o usuário escolhe o livro de seu interesse, ficando associado ao seu nome até a devolução.
Conta com uma aplicação web, desenvolvido a partir da base didática adquirida na disciplina de **Programação Orientada a Objetos (POO)**, utilizando **python, html, css** e o microframework **bottle** para a estrutura, com persistência de dados em arquivos **json**.

---

## 🗂 Estrutura de Pastas

```bash
poo-python-bottle-template/
├── app.py            # Ponto de entrada do sistema
├── config.py         # Configurações e caminhos do projeto
├── main.py           # Inicialização da aplicação
├── requirements.txt  # Dependências do projeto
├── README.md         # Este arquivo
├── controllers/      # Controladores e rotas
├── models/           # Definição das entidades (ex: User)
├── services/         # Lógica de persistência (JSON)
├── views/            # Arquivos HTML (Bottle Templating)
├── static/           # CSS, JS e imagens
├── data/             # Arquivos JSON de dados
└── .vscode/          # Configurações opcionais do VS Code
```


---

## 📁 Descrição das Pastas

### `controllers/`
Contém as classes responsáveis por lidar com as rotas da aplicação:
- `user_controller.py`: rotas para listagem, adição, edição e remoção de usuários.
- `base_controller.py`: classe base com utilitários comuns.
- `livros_controller.py`: rotas para listagem, adição, remoção e edição de livros. 

### `models/`
Define as classes que representam os dados da aplicação:
- `user.py`: classe `User`, com atributos como `id`, `name`, `email`, etc.
- `livros.py`: classe `Livro` com atributos como `id`, `name`, `author`, etc.
- `administrador.py`: classe `Adm` com atributos como `name`, `email` (herdados de `User`), `senha`, etc.

### `services/`
Responsável por salvar, carregar e manipular dados usando arquivos JSON:
- `user_service.py`: contém métodos como `get_all`, `add_user`, `delete_user`.
- `livros_service.py`: contém métodos como `save`, `edit_book`, `delete_book`.
- `relationship.py`: contém métodos como `registrar_escolha_livro`, `remover_livro_usuario`, `livros_do_usuario` (para correlacionar os livros aos usuários).

### `views/`
Contém os arquivos `.tpl` utilizados pelo Bottle como páginas HTML:
- `layout.tpl`: estrutura base com navegação e bloco `content`.
- `users.tpl`: lista os usuários.
- `user_form.tpl`: formulário para adicionar/editar usuário.
- `book.tpl`: lista os livros com suas características.
- `book_form.tpl`: formulário para adicionar/editar livro.
- `home_page`: página inicial do projeto.

### `static/`
Arquivos estáticos como:
- `css/style.css`: estilos básicos.
- `js/main.js`: scripts JS opcionais.
- `img/BottleLogo.png`: exemplo de imagem.

### `data/`
Armazena os arquivos `.json` que simulam o banco de dados:
- `users.json`: onde os dados dos usuários são persistidos.
- `books.json`: onde os dados dos livros são persistidos.
- `relationship.json`: onde os dados de qual usuário tem qual livro são persistidos.

---

## ▶️ Como Executar

1. Clone o repositório em seu computador:
```bash
git clone https://github.com/Clarice-gg/EPF-GamaDeLivros.git
```
2. Crie o ambiente virtual na pasta fora do seu projeto:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate     # Windows
```

3. Entre dentro do seu projeto criado a partir do template e instale as dependências:
```bash
pip install -r requirements.txt
```

4. Rode a aplicação:
```bash
python main.py
```

5. Accese sua aplicação no navegador em: [http://localhost:8080](http://localhost:8080)

---

## ✍️ Diagrama de Classes


---

## 🧠 Autor e Licença
Projeto desenvolvido como template didático para disciplinas de Programação Orientada a Objetos, baseado no [BMVC](https://github.com/hgmachine/bmvc_start_from_this).
Você pode reutilizar, modificar e compartilhar livremente.
