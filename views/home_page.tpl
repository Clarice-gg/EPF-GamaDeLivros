
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gama de Livros</title>
    <link rel="stylesheet" href="/static/css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@400;500&display=swap" rel="stylesheet">
    <style>
        .hero {
            text-align: center;
            padding: 40px 0;
        }
        
        .hero h1 {
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            margin-bottom: 20px;
            color: var(--accent-color);
        }
        
        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto 40px;
            color: var(--dark-color);
        }
        
        .welcome-message {
            font-size: 1.3rem;
            text-align: center;
            margin-bottom: 30px;
            color: var(--dark-color);
            font-weight: 500;
        }
        
        .access-title {
            text-align: center;
            margin-bottom: 40px;
            color: var(--dark-color);
            font-size: 1.4rem;
            position: relative;
        }
        
        .access-title:after {
            content: "";
            display: block;
            width: 80px;
            height: 3px;
            background: var(--accent-color);
            margin: 15px auto 0;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="hero">
            <h1>Gama de Livros</h1>
            <p>Sua biblioteca para encontrar um universo de conhecimento e histórias fascinantes</p>
        </div>
        
        <div class="welcome-message">
            Seja bem-vindo(a) ao Gama de Livros!
        </div>
        
        <div class="access-title">
            Como gostaria de acessar a biblioteca?
        </div>
        
        <div class="access-cards">
            <div class="access-card">
                <h3>Usuário</h3>
                <a href="/users" class="btn">Acessar</a>
            </div>
            
            <div class="access-card">
                <h3>Administrador</h3>
                <a href="/books" class="btn btn-outline">Acessar</a>
            </div>
        </div>
    </div>
</body>
</html>



