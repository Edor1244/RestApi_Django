from rest_framework import serializers
from models import Cartas


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project 
        fields = ('id', 'name', 'cardType', 'description')
       
