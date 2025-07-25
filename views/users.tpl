%rebase('layout', title='Usuários')

<section class="users-section">
    <div class="section-header" style="text-align: center;">
        <h1 class="section-title"><i class="fas fa-users"></i> Lista de Usuários</h1>
        <a href="/users/add" class="btn btn-primary">
            <i class="fas fa-plus"></i> Novo Usuário
        </a>
    </div>

    <div class="section-header" style="text-align: center;">
        <a href="/">
            <button>Voltar ao início</button>
        </a>
    </div>

    <div class="table-container">
        <table class="styled-table">
            
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Email</th>
                    <th>Data Nasc.</th>
                    <th>Livros</th>
                    <th>Ações</th>
                </tr>
            </thead>

            <tbody>
                % for u in users:
                <tr>
                    <td style="padding: 10px;">{{u.id}}</td>
                    <td style="padding: 10px;">{{u.name}}</td>
                    <td style="padding: 10px;"><a href="mailto:{{u.email}}">{{u.email}}</a></td>
                    <td style="padding: 10px;">{{u.birthdate}}</td>
                    <td style="padding: 10px; text-align: center;">{{u.books}}</td>
                    
                    <td style="padding: 10px;" class="actions">
                        <a href="/users/edit/{{u.id}}" class="btn btn-sm btn-edit">
                            <i class="fas fa-edit"></i> Editar dados
                        </a>

                        <a href="/users/{{u.id}}/books">
                            <button>Ver livros</button>
                        </a>

                        <form action="/users/delete/{{u.id}}" method="post" 
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