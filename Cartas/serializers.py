from rest_framework import serializers
from .models import User, Card, UserCard


class UserCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCard
        fields = ('user', 'name', 'card_type', 'description')
        read_only_fields = ('created_at', )


class CardSerializer(serializers.ModelSerializer):
    users = UserCardSerializer(many=True, read_only=True)

    class Meta:
        model = Card
        fields = ('card_id', 'users')
        read_only_fields = ('created_at', )


class UserSerializer(serializers.ModelSerializer):
    User_Cards = UserCardSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('user_id', 'User_Cards')
        read_only_fields = ('created_at', )
