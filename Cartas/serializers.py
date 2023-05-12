from rest_framework import serializers
from .models import User, Card, UserCard


class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCard
        fields = ('name', 'cardType', 'description')
       

class CardSerializer(serializers.ModelSerializer):
    users = UserCardSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = ('cardId', 'users') 


class UserSerializer(serializers.ModelSerializer):
    UserCards = UserCardSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('userId', 'userCard')
