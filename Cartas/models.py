from django.db import models


class Card(models.Model):
    cardId = models.CharField(max_length=200, primary_key=True)
    
    def __str__(self):
        return self.cardId


class User(models.Model):
    userId = models.CharField(max_length=200, primary_key=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='users')
    
    def __str__(self):
        return self.userId


class UserCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercards')
    name = models.CharField(max_length=200)
    cardType = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
