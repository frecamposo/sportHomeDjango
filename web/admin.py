from django.contrib import admin
from .models import Persona,UserProfile,Marcas,Articulo,Categoria
# Register your models here.

admin.site.register(Persona)
admin.site.register(UserProfile)
admin.site.register(Marcas)
admin.site.register(Articulo)
admin.site.register(Categoria)