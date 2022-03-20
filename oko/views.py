from django.shortcuts import render
from .models import *
from django.shortcuts import redirect


# Create your views here.


def start(request):

    return render(request, 'index.html')

def create_deck(request):

 ''' Create a list of playing cards in our database '''
 COLORS = [('\u2664','p'),('\u2662','dz'), ('\u2661','k'),('\u2667','t')] # pik dzwonek, kier trefl

 VALUES  =   ['2','3','4','5','6','7','8','9','10','j','q','k','a']
 cards = [Card(name=value, color=color[0], namecolor = color[1]) for color in COLORS  for value in VALUES]

 if len(Card.objects.all()) == 0:
    Card.objects.bulk_create(cards)
    return render(request, 'success.html'  )
 else:
     return render(request, 'deck_done.html')
 return render(request, 'deck.html')

def show_deck(request):
    cards = Card.objects.all()
    return render(request, 'show_deck.html', {'cards':cards})


def admin(request):
    return redirect('/admin/')