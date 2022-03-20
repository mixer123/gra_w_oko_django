from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib import admin


app_name = 'oko'
urlpatterns = [
    path('', views.start, name='start'),

   ]
