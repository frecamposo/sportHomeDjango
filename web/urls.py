
from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('',index,name='IND'),
    path('quienes_somos/',quienes_somos,name='QS'),
    path('admin_producto',admin_prod),
]
