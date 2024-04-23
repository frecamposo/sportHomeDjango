
from django.contrib import admin
from django.urls import path, include
from .viewLogin import *
from .views import listas_marcas
urlpatterns = [
    path('logines/',login,name='logines'),
    path('lista_marcas/',listas_marcas,name='LM'),
    
]
