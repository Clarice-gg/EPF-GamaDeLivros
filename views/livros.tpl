%rebase('layout', title='Livros do usuário')

<section>
    <div>
        <a href="/users">
            <button>Voltar aos usuários</button>
        </a>
    </div>

    <div style="text-align: center;">
        <h1>Livros disponíveis para escolher</h1>
        <ul>
            % for book in livros_disponiveis:
            <li>
            <strong>{{book["name"]}}</strong>
            <form action="/users/{{user["id"]}}/books/{{book["id"]}}/escolher" method="post">
                <button type="submit">Escolher</button>
            </form>
            </li>
            % end
        </ul>
    </div>

    <div style="text-align: center;">
    <h1>Livros já escolhidos</h1>
    <ul>
        % for book in livros_escolhidos:
        <li>
            <strong>{{book["name"]}}</strong>

<!-- tá com erro aqui também (na linha abaixo) REVISAR -->
            <form action="/users/{{user["id"]}}/books/{{book["id"]}}/remover" method="post">
                <button type="submit">Remover</button>
            </form>
        </li>
        % end
    </ul>
    </div>
</section>