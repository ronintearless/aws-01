from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def backpack(request):
    return render(request, 'backpack.html')