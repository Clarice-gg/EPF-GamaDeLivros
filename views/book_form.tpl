% rebase('layout', title='Formulário Livros')

<section class="form-section">
    <h1>{{'Editar Livro' if book else 'Adicionar Livro'}}</h1>

    <form action="{{action}}" method="post" class="form-container">
        <div class="form-group">
            <label for="name">Nome:</label>
            <input type="text" id="name" name="name" required 
                   value="{{book.name if book else ''}}">
        </div>

        <div class="form-group">
            <label for="name">Autor:</label>
            <input type="text" id="author" name="author" required 
                   value="{{book.author if book else ''}}">
        </div>

        <div class="form-group">
            <label for="name">Paginas:</label>
            <input type="text" id="pages" name="pages" required 
                   value="{{book.pages if book else ''}}">
        </div>

        <div class="form-group">
            <label for="name">Quantidade:</label>
            <input type="text" id="name" name="stock" required 
                   value="{{book.stock if book else ''}}">
        </div>

        <div class="form-actions">
            <button type="submit" class="btn-submit">Salvar</button>
            <a href="/books" class="btn-cancel">Voltar</a>
        </div>
    </form>
</section>