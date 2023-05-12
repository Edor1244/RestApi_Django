from django.db import models

# Create your models here.


class Cartas(models.Model):
    useriD = models.ManyToManyField('User')

    def __str__(self):
        return self.user
    

class User(models.Model):
    useriD = models.CharField(max_length=200)
    cardId = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


class UserCards(models.Model):
    cardId = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=200)
    cardType = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name
