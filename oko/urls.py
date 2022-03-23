from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib import admin


app_name = 'oko'
urlpatterns = [
    path('', views.start, name='start'),
    path('create_deck/', views.create_deck, name='create_deck'),
    path('show_deck/', views.show_deck, name='show_deck'),
    path('take_cards/', views.take_cards, name='take_cards'),
    path('show_player_cards/', views.show_player_cards, name='show_player_cards'),
    path('reset_card/', views.reset_card, name='reset_card'),
    path('take_one_card_more/', views.take_one_card_more, name='take_one_card_more'),
    path('finall_game/', views.finall_game, name='finall_game'),

   ]
