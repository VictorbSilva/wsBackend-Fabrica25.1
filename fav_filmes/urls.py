from django.urls import path
from . import views

app_name = 'filmes'

urlpatterns = [
    path('buscar_filme/', views.buscar_filme, name='buscar_filme'),
    path('adicionar_favorito/', views.adicionar_favorito, name='adicionar_favorito'),
    path('exibir_favoritos/', views.exibir_favoritos, name='exibir_favoritos'),
    path('remover_favorito/<int:pk>/', views.remover_favorito, name='remover_favorito'),
    path('editar_favorito/<int:pk>/', views.editar_favorito, name='editar_favorito'),
]


