from rest_framework import serializers
from .models import User, Card, UserCard


class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCard
        fields = ('name', 'cardType', 'description')
        read_only_fields = ('created_at', )


class CardSerializer(serializers.ModelSerializer):
    users = UserCardSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = ('cardId', 'users') 
        read_only_fields = ('created_at', )


class UserSerializer(serializers.ModelSerializer):
    UserCards = UserCardSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('userId', 'userCard')
        read_only_fields = ('created_at', )
