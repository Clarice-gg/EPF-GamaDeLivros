%rebase('layout', title='Livros do usuário')

<section>
    <div>
        <a href="/users" style="text-align: center;">
            <button>Voltar aos usuários</button>
        </a>
    </div>

    <div>
        <h1 style="text-align: center;">Livros disponíveis para empréstimo</h1>
        <ul>
            % for book in livros_disponiveis:
            <li>
            <strong>{{book["name"]}}</strong>
            <form action="/users/{{user_id}}/books/{{book["id"]}}/escolher" method="post">
                <button type="submit">Escolher</button>
            </form>
            </li>
            % end
        </ul>
    </div>

    <div>
    <h1 style="text-align: center;">Livros já escolhidos</h1>
    <ul>
        % for book in livros_escolhidos:
        <li>
            <strong>{{book["name"]}}</strong>

<!-- tá com erro aqui também (na linha abaixo) REVISAR -->
            <form action="/users/{{user_id}}/books/{{book["id"]}}/remover" method="post">
                <button type="submit">Remover</button>
            </form>
        </li>
        % end
    </ul>
    </div>
</section>