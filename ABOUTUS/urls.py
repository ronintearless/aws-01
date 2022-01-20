from django.urls import path

from . import views

app_name = 'ABOUTUS'

urlpatterns = [
    path('', views.aboutus , name='aboutus'),
    path('', views.index , name='index'),
]