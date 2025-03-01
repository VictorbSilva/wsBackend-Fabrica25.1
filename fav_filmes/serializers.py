from rest_framework import serializers
from .models import FilmeModel, FavoritoModel

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmeModel
        fields = '__all__'
    
        
class FavoritoSerializer(serializers.ModelSerializer):
    filme_favorito = FilmeSerializer(read_only=True)
    id_filme_imdb = serializers.CharField(write_only=True)
    nota = serializers.DecimalField(max_digits=2, decimal_places=1, required=False, allow_null=True, min_value=0.0, max_value=10.0)
    
    class Meta:
        model = FavoritoModel
        fields = ['id', 'filme_favorito', 'nota_usuario', 'data_adicao','id_filme_imdb']
        read_only_fields = ['data_adicao']
    
    def CriaFilme(self, validated_data):
        id_imdb = validated_data.pop('id_filme_imdb')
        usuario = self.context['request'].user
        
        filme, _ = FilmeModel.objects.get_or_create(
            id_imdb = id_imdb,
            defaults={
                'titulo_filme': validated_data.get('titulo_filme', ''),
                'ano': validated_data.get('ano', 0),
                'diretor': validated_data.get('diretor', ''),
                'genero': validated_data.get('genero', ''),
                'sinopse': validated_data.get('sinopse', ''),
                'nota_imdb':validated_data.get('nota_imdb', 0.0),
            }
        )
        
        favorito = FavoritoModel.objects.create(usuario=usuario, filme_favorito=filme, nota_usuario=validated_data.get('nota_usuario', None))
        return favorito
    
    def dados_filme(self, id_imdb):
        try:
            filme = FilmeModel.objects.get(id_imdb=id_imdb)
            return FilmeSerializer(filme).data
        except FilmeModel.DoesNotExist:
            return None