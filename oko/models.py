from django.db import models

# Create your models here.

POSSIBLE_VALUES  = (
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("J", "J"),
    ("K", "K"),
    ("Q", "Q"),
    ("A", "A"),
)

POSSIBLE_COLORS = (
    ('sapdes', '\u2664'),
    ('diamonds', '\u2662'),
    ('hearts', '\u2661'),
    ('clubs', '\u2667'),
)

class Card(models.Model):
    name = models.CharField(max_length=100,choices = POSSIBLE_VALUES, unique=True, verbose_name='')
    color = models.CharField(max_length=100, choices=POSSIBLE_COLORS, unique=True, verbose_name='')


    def __str__(self):
        self.name

    class Meta:
        abstract = True