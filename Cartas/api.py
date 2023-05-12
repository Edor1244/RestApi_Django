from .models import User, Card, UserCard
from rest_framework import viewsets, permissions
from .serializers import CardSerializer, UserCardSerializer, UserSerializer


class CartasViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CardSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserCardsViewSet(viewsets.ModelViewSet):
    queryset = UserCard.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserCardSerializer




