from django.contrib import admin
from .models import Persona,UserProfile,Marcas,Articulo
# Register your models here.

admin.site.register(Persona)
admin.site.register(UserProfile)
admin.site.register(Marcas)
admin.site.register(Articulo)