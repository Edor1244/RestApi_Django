from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=200, primary_key=True)
    
    def __str__(self):
        return self.user_id


class Card(models.Model):
    card_id = models.CharField(max_length=200, primary_key=True)
    users = models.ManyToManyField(User, through='UserCard')
    
    def __str__(self):
        return self.card_id


class UserCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    card_type = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
