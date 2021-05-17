from sys import path

from django.shortcuts import render

# Create your views here.
import store

def index(request):
    return render(request, 'store/home.html')