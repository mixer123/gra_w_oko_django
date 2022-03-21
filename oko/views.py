from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from random import shuffle


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

def take_cards(request):
    list_cards_id = []
    cards = Card.objects.all()
    for card in cards:
        list_cards_id.append(card.id)
    shuffle(list_cards_id)
    id=list_cards_id.pop()
    card = Card.objects.get(id=id)
    Card.objects.filter(id=id).update(status=False)
    user = Player.objects.create(name='user',card=card)
    id = list_cards_id.pop()
    card = Card.objects.get(id=id)
    Card.objects.filter(id=id).update(status=False)
    user = Player.objects.create(name='user', card=card)

    # Teraz croupier losuje
    shuffle(list_cards_id)
    id = list_cards_id.pop()
    card = Card.objects.get(id=id)
    Card.objects.filter(id=id).update(status=False)
    user = Player.objects.create(name='croupier', card=card)
    id = list_cards_id.pop()
    card = Card.objects.get(id=id)
    Card.objects.filter(id=id).update(status=False)
    user = Player.objects.create(name='croupier', card=card)
    return render(request, 'take_cards.html')

def show_player_cards(request):
    user = Player.objects.filter(name='user')
    croupier = Player.objects.filter(name='croupier')
    return render(request, 'show_player_cards.html',{'user':user, 'croupier':croupier})
def admin(request):
    return redirect('/admin/')