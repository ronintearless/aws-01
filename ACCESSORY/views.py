from django.shortcuts import render,HttpResponse

def backpack(request):
    return render(request, 'backpack.html')

def index(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')

def clothes(request):
    return render(request, 'clothes.html')

def accessory(request):
    return render(request, 'accessory.html')

def aboutus(request):
    return render(request, 'aboutus.html')

