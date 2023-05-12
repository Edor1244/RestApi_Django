from .models import Cartas
from .models import User
from .models import UserCards
from rest_framework import viewsets, permissions
from .serializers import CartasSerializer
from .serializers import UserSerializer
from .serializers import UserCardsSerializer


class CartasViewSet(viewsets.ModelViewSet):
    queryset = Cartas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserCardsSerializer

    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserCardsViewSet(viewsets.ModelViewSet):
    queryset = UserCards.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CartasSerializer




