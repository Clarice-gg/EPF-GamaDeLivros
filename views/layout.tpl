<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Bottle - {{title or 'Sistema'}}</title>
    <link rel="stylesheet" href="/static/css/style.css" />
    <style>
    body {
        background-image: url("static\img\library.jpg");
        background-repeat: no-repeat;
        background-size: cover;
        background-attachment: fixed;
    }
</style>
</head>
<body>

    <div class="container" style="max-width: fit-content; margin-top: 30px; margin-bottom: 40px; margin-align: center;">
        {{!base}}  <!-- O conteúdo das páginas filhas virá aqui -->
    </div>

    <footer>
        <p style="text-align: center;">&copy; 2025, Meu Projeto. Todos os direitos reservados.</p>
    </footer>

    <!-- Scripts JS no final do body -->
    <script src="/static/js/main.js"></script>
</body>
</html>
