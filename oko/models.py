from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100,  verbose_name='')
    color = models.CharField(max_length=100,  verbose_name='')
    namecolor = models.CharField(max_length=3, verbose_name='')
    status = models.BooleanField(default=True)


    def score(self):
        sum = 0
        sum_A = 0
        sum_F = 0
        if self.name in ['j', 'k', 'q']:
           sum += 10
           sum_F += 1

        if self.name in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
           sum += int(self.name)
           if self.name == "a":
                sum_A += 1
        if sum_A == 2 or (sum_A == 1 and sum_F == 1):
            sum = 21
        return sum



    # def __str__(self):
    #     self.name

class Player(models.Model):

    name = models.CharField(max_length=100, verbose_name='')
    card = models.ForeignKey(Card, on_delete=models.CASCADE)





