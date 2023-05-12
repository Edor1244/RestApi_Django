from django.db import models

# Create your models here.


class Cartas(models.Model):
    users = models.ManyToManyField('User', related_name='cartas')

    def __str__(self):
        return self.name
    

class User(models.Model):
    useriD = models.CharField(max_length=200)
    User_Cards = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


class UserCards(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=200)
    cardType = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    


    

