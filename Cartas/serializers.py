from rest_framework import serializers
from .models import Cartas


class CartasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartas
        fields = ('id', 'name', 'cardType', 'description')
        read_only_fields = ('created_at', )    
