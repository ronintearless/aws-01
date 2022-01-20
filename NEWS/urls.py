from django.urls import path

from . import views

app_name = 'NEWS'

urlpatterns = [
    path('', views.news , name='news'),
    path('', views.index , name='index'),
]