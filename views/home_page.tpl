<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Gama de livros</title>
    <!-- CSS para o tema -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">

    <!-- JS da biblioteca -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>

    <!-- Suporte a linguagens específicas (Python e HTML) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/xml.min.js"></script>

    <!-- Ativa o realce automaticamente -->
    <script>hljs.highlightAll();</script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background: #f9f9f9;
            color: #333;
        }
        h1, h2 {
            color:rgb(30, 31, 32);
        }
        button {
            background-color:rgb(92, 65, 38)
        }
        section {
            margin-bottom: 20px;
        }
        .comment {
            background-color: #f8f8f8;
            padding: 10px;
            border-bottom: 4px solid rgb(92, 65, 38);
            margin-bottom: 10px;
            font-style: italic;
        }
    </style>
</head>
<!--AINDA TEM QUE CENTRALIZAR OS BOTÕES-->

<body>
<h1 style="text-align: center;">Gama de livros</h1>
<div class="comment"></div>

<section>
    <div class="section-header" style="text-align: center;">
        <h1 class="section-title"></i>Seja bem-vindo(a) ao Gama de livros!</h1>
    </div>

    <div class="section-header" style="text-align: center;">
        <h4>Como gostaria de acessar a biblioteca?</h4>
    </div>

    <div class="table-container" style="padding-left: 585px; padding-top: 20px;">
        <table class="styled-table">

            <thead>
                <tr>
                    <th style="font-size: 20px;">Usuário</th>
                    <th style="padding-left: 50px; font-size: 20px;">Administrador</th>
                </tr>
            </thead>

            <tbody>
                
                <tr>
                    <td style="padding: 10px; text-align: center;">
                        <a href="/users">
                            <button style="color: white;">Acessar</button>
                        </a>
                    </td>
                    <td style="padding: 10px; padding-left:50px; text-align: center;">
                        <a href="/books">
                            <button style="color: white;">Acessar</button>
                        </a>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</section>
</body>
