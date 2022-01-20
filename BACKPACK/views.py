from django.shortcuts import render
from .models import *


def index(request):
    context = {}
    return render(request, 'index.html', context)

def backpack(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'backpack.html', context)

def news(request):
    return render(request, 'news.html')

def clothes(request):
    return render(request, 'clothes.html')

def accessory(request):
    return render(request, 'accessory.html')

def aboutus(request):
    return render(request, 'aboutus.html')

