from .models import Cartas
from rest_framework import viewsets, permissions
from serializers import CartasSerializer


class CartasViewSet(viewsets.ModelViewSet):
    queryset = Cartas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CartasSerializer
