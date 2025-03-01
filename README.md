# FavFilmes 🎬

Aplicação web para buscar, favoritar e gerenciar filmes usando a API do OMDB. Desenvolvido com Django e PostgreSQL.

## Funcionalidades ✨
- 🔍 Busca de filmes em tempo real
- ❤️ Sistema de favoritos pessoais
- ⭐ Atribuição de notas aos filmes
- 👤 Autenticação de usuários
- 📊 Gestão de dados com PostgreSQL

## Pré-requisitos 📋
- Python 3.9+
- PostgreSQL 15+
- Git
- Chave da API OMDB ([obtenha gratuitamente](https://www.omdbapi.com/apikey.aspx))

## Instalação Passo a Passo 🚀

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/favfilmes.git
cd favfilmes

2. Crie um ambiente virtual
bash
Copy

python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows

3. Instale as dependências
bash
Copy

pip install -r requirements.txt

4. Configure o banco de dados

    Crie um banco PostgreSQL:

sql
Copy

CREATE DATABASE favfilmesDB;
CREATE USER victo WITH PASSWORD 'sua_senha_segura';
GRANT ALL PRIVILEGES ON DATABASE favfilmesDB TO victo;

5. Configure as variáveis de ambiente

Crie um arquivo .env na raiz do projeto:
ini
Copy

OMDB_API_KEY=sua_chave_omdb
DATABASE_URL=postgres://victo:sua_senha_segura@localhost:5432/favfilmesDB

6. Aplique as migrações
bash
Copy

python manage.py migrate

7. Crie um usuário admin
bash
Copy

python manage.py createsuperuser

8. Inicie o servidor
bash
Copy

python manage.py runserver

Acesse: http://localhost:8000
Como Usar 🖱️
Login

    Acesse /accounts/login/

    Use as credenciais do superusuário criado

Buscar Filmes

    Na página inicial, clique em "Buscar Filme"

    Digite o título desejado

    Veja os resultados da pesquisa

Busca
Adicionar Favoritos

    Nos resultados da busca:

    Insira uma nota (opcional)

    Clique em "Favoritar"

Gerenciar Favoritos

    Editar: Altere sua nota

    Remover: Exclua da lista

    Visualizar: Veja todos em "Meus Favoritos"

Estrutura do Projeto 📂
Copy

favfilmes/
├── fav_filmes/          # Aplicação principal
│   ├── templates/       # Telas da aplicação
│   ├── models.py        # Modelos de dados
│   ├── views.py         # Lógica das páginas
├── projeto/             # Configurações Django
├── requirements.txt     # Dependências
└── .env.example         # Modelo de variáveis de ambiente
