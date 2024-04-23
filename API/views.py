from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from web.models import Marcas
from .serializers import MarcasSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listas_marcas(request):
    if request.method == 'GET':
        marcas = Marcas.objects.all()
        serializer = MarcasSerializers(marcas,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer= MarcasSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)