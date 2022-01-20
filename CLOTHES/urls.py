from django.urls import path

from . import views

app_name = 'CLOTHES'

urlpatterns = [
    path('', views.clothes , name='clothes'),
    path('', views.index , name='index'),
]