from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from web.models import Marcas,Categoria,Articulo
from .serializers import MarcasSerializers,CategoriaSerializers,ArticuloSerializers

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

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def listas_categorias(request):
    if request.method == 'GET':
        catego = Categoria.objects.all()
        serializer = CategoriaSerializers(catego,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer= CategoriaSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def opt_articulos(request,id_articulo):
    try:
        art = Articulo.objects.get(id=id_articulo)
    except Inventario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #art = Articulo.objects.all()
        serializer = ArticuloSerializers(art,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer= ArticuloSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        serializer = ArticuloSerializers(art, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_articulos(request):
    try:
        art = Articulo.objects.all()
    except Inventario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #art = Articulo.objects.all()
        serializer = ArticuloSerializers(art,many=True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
