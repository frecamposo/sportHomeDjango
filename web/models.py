from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=20)
    edad= models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Marcas(models.Model):
    nombre = models.CharField(max_length=200,primary_key=True)
    
    def __str__(self):
        return self.nombre
    
class Articulo(models.Model):
    codigo = models.CharField(max_length=200,primary_key=True)
    marca =  models.ForeignKey(Marcas, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200,null=False)
    description = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    role = models.CharField(max_length=20,choices=settings.ROLE)
    
    def __str__(self):
        return self.user.username+ ' '+self.role
