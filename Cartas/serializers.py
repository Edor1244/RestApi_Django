from rest_framework import serializers
from .models import User
from .models import Cartas
from .models import UserCards


class CartasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartas
        fields = ('users')
        read_only_fields = ('created_at', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('useriD', 'User_Cards')
        read_only_fields = ('created_at', )    


class UserCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCards
        fields = ('id', 'name', 'cardType', 'description')
        read_only_fields = ('created_at', )