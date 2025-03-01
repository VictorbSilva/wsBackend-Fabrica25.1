# FavFilmes 🎬

Uma aplicação web para buscar, favoritar e gerenciar filmes usando a API do OMDB. Desenvolvido com Django, PostgreSQL e Docker.

## Funcionalidades Principais 🔍

### 1. Busca de Filmes
- Pesquise filmes pelo título usando dados em tempo real da API OMDB
- Visualize detalhes como diretor, ano, sinopse e nota IMDB
- Interface responsiva com cards para cada resultado

### 2. Sistema de Favoritos
- Adicione filmes à sua lista pessoal
- Atribua notas de 0 a 10 para cada filme favoritado
- Edite ou remova favoritos facilmente

### 3. Autenticação de Usuário
- Sistema seguro de login/logout
- Listas de favoritos individuais por usuário
- Proteção contra CSRF e SQL injection

### 4. Gestão de Dados
- Armazenamento em banco de dados PostgreSQL
- CRUD completo para filmes e favoritos
- Validação de dados em formulários

## Tecnologias Utilizadas 🛠️

**Backend**
- Python 3.13.2
- Django 5.1
- Django REST Framework
- PostgreSQL
- Docker

**Frontend**
- HTML5 semântico
- CSS customizado
- Sistema de templates Django
- Design responsivo

## Pré-requisitos 📋

- Docker 20.10+
- Docker Compose 2.20+
- Chave de API OMDB (gratuita)

## Instalação Local 🚀

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/favfilmes.git
cd favfilmes

    Configure as variáveis de ambiente

bash
Copy

cp .env.example .env
# Edite o .env com suas credenciais

    Inicie os containers

bash
Copy

docker-compose up -d --build

    Execute as migrações

bash
Copy

docker-compose exec web python manage.py migrate

    Crie um superusuário

bash
Copy

docker-compose exec web python manage.py createsuperuser

    Acesse a aplicação

Copy

http://localhost:8000

Guia de Uso 📖
Página Inicial

    Buscar Filmes: Inicie novas pesquisas

    Favoritos: Acesse sua lista pessoal

    Login/Logout: Gerencie sua sessão

Home
Pesquisa de Filmes

    Digite o título do filme

    Clique em "Buscar"

    Visualize os resultados

Adicionar Favorito

    Na lista de resultados:

    Defina sua nota (opcional)

    Clique em "Favoritar"

Gerenciar Favoritos

    Editar Nota: Atualize sua avaliação

    Remover: Exclua da lista

    Ordenação: Automática por data de adição

Favoritos
Estrutura do Projeto 📂
Copy

favfilmes/
├── fav_filmes/          # App principal
│   ├── templates/       # Telas da aplicação
│   ├── models.py        # Definição de modelos
│   ├── views.py         # Lógica das páginas
│   └── serializers.py   # API REST
│
├── projeto/             # Configurações Django
├── docker-compose.yml   # Orquestração de containers
└── requirements.txt     # Dependências Python
