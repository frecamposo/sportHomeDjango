from rest_framework import serializers
from web.models import Articulo,Marcas

class MarcasSerializers(serializers.ModelSerializer):
    class Meta:
        model =Marcas
        fields = ['nombre']
        
        