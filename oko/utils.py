from django.db import models
from models import Card

def create_deck():
 ''' Create a list of playing cards in our database '''
 COLORS = ['\u2664','\u2662', '\u2661','\u2667']
 VALUES  =   ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
 cards = [Card(name=VALUES, color=COLORS) for color in COLORS for value in VALUES]
 Card.objects.bulk_create(cards)