from django.urls import path

from . import views

app_name = 'ACCESSORY'

urlpatterns = [
    path('', views.accessory , name='accessory'),
    path('', views.index , name='index'),
]