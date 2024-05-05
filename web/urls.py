
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('',index,name='IND'),
    path('quienes_somos/',quienes_somos,name='QS'),
    path('tenis/',tenis,name='TE'),
    path('natacion/',natacion,name='NA'),
    path('basquet/',basquetball,name='BB'),
    path('futbol/',futbol,name='FB'),
    path('voley/',voleyball,name='VB'),
    path('sucursales/',sucursales,name='SU'),
    path('producto/',producto,name='PR'),
    path('login/',login,name='LG'),
    path('registro/',grabar_usuario,name='RE'),
    path('cerrar/',cerrar_sesion,name='CS'),

    path('articulos/',articulos,name='ART'),
    path('agregar/',agregar,name='AGR'),
    path('eliminar/<id>/',eliminar,name='ELI'),
    path('modificar/<id>/',modificar_buscar,name='MOD'),
    path('modificar_datos/',modificar,name='MODI'),
    path('articulos_api/',form_api,name='ART_API'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
