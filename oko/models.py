from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100,  verbose_name='')
    color = models.CharField(max_length=100,  verbose_name='')
    namecolor = models.CharField(max_length=3, verbose_name='')
    status = models.BooleanField(default=True)
    # def __str__(self):
    #     self.name

class Player(models.Model):

    name = models.CharField(max_length=100, verbose_name='')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)



