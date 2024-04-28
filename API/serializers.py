from rest_framework import serializers
from web.models import Articulo,Marcas,Categoria

class MarcasSerializers(serializers.ModelSerializer):
    class Meta:
        model =Marcas
        fields = ['nombre']
        
class CategoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model =Categoria
        fields = '__all__'

class ArticuloSerializers(serializers.ModelSerializer):
    class Meta:
        model =Articulo
        fields = '__all__'
