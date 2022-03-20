from django.shortcuts import render
from .models import *
from django.shortcuts import redirect

# Create your views here.


def start(request):

    return render(request, 'index.html')


def admin(request):
    return redirect('/admin/')