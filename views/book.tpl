%rebase('layout', title='Livros')

<section class="users-section">
    <div class="section-header">
        <h1 class="section-title"><i class="fas fa-users"></i> Lista de Livros</h1>
        <a href="/books/add" class="btn btn-primary">
            <i class="fas fa-plus"></i> Novo Livro
        </a>
    </div>

    <div class="table-container">
        <table class="styled-table">

            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Autor</th>
                    <th>Paginas</th>
                    <th>Quantidade</th>
                    <th>Ações</th>
                </tr>
            </thead>

            <tbody>
                % for u in books:
                <tr>
                    <td style="padding: 10px;">{{u.id}}</td>
                    <td style="padding: 10px;">{{u.name}}</td>
                    <td style="padding: 10px;">{{u.author}}</td>
                    <td style="padding: 20px;">{{u.pages}}</td>
                    <td style="padding: 30px;">{{u.stock}}</td>

                    <td style="padding: 20px;" class="actions">
                        <a href="/books/edit/{{u.id}}" class="btn btn-sm btn-edit">
                            <i class="fas fa-edit"></i> Editar
                        </a>

                        <form action="/books/delete/{{u.id}}" method="post" 
                              onsubmit="return confirm('Tem certeza?')">
                            <button type="submit" class="btn btn-sm btn-danger">
                                <i class="fas fa-trash-alt"></i> Excluir
                            </button>
                        </form>
                    </td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</section>