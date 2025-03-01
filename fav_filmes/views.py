from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import FilmeModel, FavoritoModel
from django.urls import reverse
import requests


def index(request):
    return render(request, 'fav_filmes/index.html')

def login_usuario(request):
    mensagem = None
    if request.method == 'POST':
        usuario = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(username=usuario, password=senha)
        if user:
            login(request, user)
            return redirect('filmes:buscar_filme')  # Use o nome da URL corretamente
        else:
            mensagem = 'Usuário ou senha inválidos.'
    return render(request, 'login.html')

def buscar_filme(request):
    filmes = None
    mensagem = None
    
    if request.method == 'POST':
        titulo_filme = request.POST.get('titulo')
        api_key = '72fdc024'
        url = f'http://www.omdbapi.com/?apikey={api_key}&s={titulo_filme}'
        
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            
            if dados['Response'] == 'True':
                return render(request, 'fav_filmes/resultados_busca.html', {'filmes': dados['Search'], 'titulo_filme': titulo_filme})
            else:
                return render(request, 'fav_filmes/buscar_filme.html', {'mensagem': 'Filme não encontrado'})
    return render(request, 'fav_filmes/buscar_filme.html', {'filmes': filmes, 'mensagem': mensagem})

@login_required
def adicionar_favorito(request):
    if request.method == 'POST':
        id_imdb = request.POST.get('id_imdb')
        nota = request.POST.get('nota', 0.0)
        
        # Busca os dados do filme na OMDB API
        dados_filme = requests.get(f'http://www.omdbapi.com/?apikey=72fdc024&i={id_imdb}').json()
        
        # Trata campos que podem ser 'N/A'
        nota_imdb = dados_filme.get('imdbRating', '0.0')
        if nota_imdb == 'N/A':
            nota_imdb = 0.0  # Valor padrão
            
        ano = dados_filme.get('Year', '0')
        if ano == 'N/A':
            ano = 0
        else:
            ano = int(ano.replace('-', '0')[:4])  # Garante que é um inteiro
        
        # Trata outros campos para evitar 'N/A'
        diretor = dados_filme.get('Director', 'Diretor não disponível').strip()
        if diretor == 'N/A':
            diretor = 'Diretor não disponível'
            
        genero = dados_filme.get('Genre', 'Gênero não disponível').strip()
        if genero == 'N/A':
            genero = 'Gênero não disponível'
            
        sinopse = dados_filme.get('Plot', 'Sinopse não disponível').strip()
        if sinopse == 'N/A':
            sinopse = 'Sinopse não disponível'
        
        # Cria ou atualiza o filme no banco de dados
        filme, _ = FilmeModel.objects.update_or_create(
            id_imdb=id_imdb,
            defaults={
                'titulo_filme': dados_filme.get('Title', 'Sem título').strip(),
                'ano': ano,
                'diretor': diretor,
                'genero': genero,
                'sinopse': sinopse,
                'nota_imdb': float(nota_imdb)  # Agora seguro
            }
        )
        
        # Cria o favorito
        FavoritoModel.objects.create(
            usuario=request.user,
            filme_favorito=filme,
            nota_usuario=nota
        )
        
        return redirect('filmes:exibir_favoritos')
    
    return redirect('filmes:buscar_filme')

@login_required
def exibir_favoritos(request):
    favoritos = FavoritoModel.objects.filter(usuario=request.user)
    return render(request, 'fav_filmes/lista_favoritos.html', {'favoritos': favoritos})

@login_required
def remover_favorito(request, pk):
    FavoritoModel.objects.filter(id=pk, usuario=request.user).delete()
    return redirect('filmes:exibir_favoritos')

@login_required
def editar_favorito(request, pk):
    favorito = FavoritoModel.objects.get(id=pk, usuario=request.user)
    if request.method == 'POST':
        nota = request.POST.get('nota')
        if nota:
            favorito.nota_usuario = nota
            favorito.save()
        return redirect('filmes:exibir_favoritos')
    return render(request, 'fav_filmes/editar_favorito.html', {'favorito': favorito})
# Create your views here.
