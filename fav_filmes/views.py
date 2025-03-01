from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import FilmeModel, FavoritoModel
from django.urls import reverse
import requests


def index(request):
    return render(request, 'index.html')

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
                return render(request, 'resultados_busca.html', {'filmes': dados['Search'], 'titulo_filme': titulo_filme})
            else:
                return render(request, 'buscar_filme.html', {'mensagem': 'Filme não encontrado'})
    return render(request, 'buscar_filme.html', {'filmes': filmes, 'mensagem': mensagem})

@login_required
def adicionar_favorito(request):
    if request.method == 'POST':
        id_imdb = request.POST.get('id_imdb')
        nota = request.POST.get('nota', 0.0)
        
        filme_existente = FilmeModel.objects.filter(id_imdb=id_imdb).first()
        
        if filme_existente:
            ja_favoritado = FavoritoModel.objects.filter(
                usuario=request.user, 
                filme_favorito=filme_existente
            ).exists()
            
            if ja_favoritado:
                
                resposta = requests.get(f'http://www.omdbapi.com/?apikey=72fdc024&s={request.POST.get("titulo_filme")}')
                filmes = resposta.json().get('Search', [])
                return render(request, 'resultados_busca.html', {
                    'filmes': filmes,
                    'erro': 'Este filme já está em seus favoritos!'
                })

        
        dados_filme = requests.get(f'http://www.omdbapi.com/?apikey=72fdc024&i={id_imdb}').json()
        
        filme, _ = FilmeModel.objects.update_or_create(
            id_imdb=id_imdb,
            defaults={
                'titulo_filme': dados_filme.get('Title', ''),
                'ano': int(dados_filme.get('Year', '0').replace('-', '0')[:4]),
                'diretor': dados_filme.get('Director', ''),
                'genero': dados_filme.get('Genre', ''),
                'sinopse': dados_filme.get('Plot', ''),
                'nota_imdb': float(dados_filme.get('imdbRating', 0.0))
            }
        )
        
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
    return render(request, 'lista_favoritos.html', {'favoritos': favoritos})

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
    return render(request, 'editar_favorito.html', {'favorito': favorito})
# Create your views here.
