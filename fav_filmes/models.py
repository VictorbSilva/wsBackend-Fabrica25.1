from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

class FilmeModel(models.Model):
    id_imdb = models.CharField(max_length=20, primary_key=True)
    titulo_filme = models.CharField(max_length=100)
    ano = models.IntegerField()
    diretor = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    sinopse = models.TextField()
    nota_imdb = models.DecimalField(max_digits=3, decimal_places=1)
    
    def __str__(self):
        return f'{self.titulo_filme} ({self.ano})'
    
    
class FavoritoModel(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    filme_favorito = models.ForeignKey(FilmeModel, on_delete=models.CASCADE)
    nota_usuario = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(10)])
    data_adicao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['usuario', 'filme_favorito']
        
    def __str__(self):
        return f"{self.usuario} - {self.filme_favorito}"
# Create your models here.
