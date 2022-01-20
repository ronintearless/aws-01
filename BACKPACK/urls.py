from django.urls import path

from . import views

app_name = 'BACKPACK'

urlpatterns = [
    path('', views.backpack , name='backpack'),
    path('', views.index , name='index'),
]