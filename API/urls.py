
from django.contrib import admin
from django.urls import path, include
from .viewLogin import *
from .views import *
urlpatterns = [
    path('logines/',login,name='logines'),
    path('lista_marcas/',listas_marcas,name='LM'),
    path('listas_categorias/',listas_categorias,name='LC'),
    path('operaciones_articulos/<id_articulo>',opt_articulos,name='OA'),
    path('lista_articulos/',lista_articulos,name='LA'),
]
