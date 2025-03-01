from rest_framework import viewsets
from .models import FilmeModel, FavoritoModel
from .serializers import FilmeSerializer, FavoritoSerializer
from rest_framework.permissions import IsAuthenticated

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = FilmeModel.objects.all()
    serializer_class = FilmeSerializer
    
class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = FavoritoModel.objects.all()
    serializer_class = FavoritoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)