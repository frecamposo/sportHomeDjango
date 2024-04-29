from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login as login_aut,logout
from django.contrib.auth.decorators import login_required,permission_required
from .models import Marcas, Articulo,Categoria, UserProfile
from django.contrib.auth.models import User
# Create your views here. (metodo en python que permita render de pag web)
import requests
def index(request): 
    return render(request, 'core/index.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

@login_required(login_url='/login/')
def futbol(request):
    return render(request, 'core/futbol.html')

@login_required(login_url='/login/')
def basquetball(request):
    return render(request, 'core/basquetball.html')

@login_required(login_url='/login/')
def natacion(request):
    return render(request, 'core/natacion.html')

@login_required(login_url='/login/')
def tenis(request):
    cate = Categoria.objects.get(nombre='tenis')
    arti = Articulo.objects.all().filter(categoria=cate)
    print(arti)
    contexto={"articulos":arti}
    return render(request, 'core/tenis.html',contexto)

@login_required(login_url='/login/')
def voleyball(request):
    return render(request, 'core/voleyball.html')

@login_required(login_url='/login/')
def sucursales(request):
    return render(request, 'core/sucursales.html')

@login_required(login_url='/login/')
def producto(request):
    return render(request, 'core/producto.html')

def grabar_usuario(request):
    contexto={}
    if request.POST:
        Usuario=request.POST.get('Usuario')
        Password=request.POST.get('Password')
        Nombre=request.POST.get('Nombre')
        Email=request.POST.get('Email')
        Apellido=request.POST.get('Apellido')
        try:
            us= User()
            us.username=Usuario
            us.first_name=Nombre
            us.last_name=Apellido
            us.email= Email
            us.set_password(Password)
            us.save()
            contexto["mensaje"]="usuario Grabado"
        except:
            contexto["mensaje"]="problemas al grabar el usuario, revise sus datos"
    return render(request,"core/registro.html",contexto)
        
def login(request):
    contexto={}
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        user = authenticate(request,username=usuario,password=password)
        print("usuario:",usuario)
        print("pass",password)
        if user is not None:
            profile = UserProfile.objects.get(user=user)
            request.session["perfil"]=profile.role
            print(profile.role)
            login_aut(request,user)
            return render(request,'core/index.html')
        else:
            contexto["mensaje"]="usuario o Contraseña Incorrecta"
    return render(request, 'core/login.html',contexto)


def registro(request):
    return render(request, 'core/registro.html')

@login_required(login_url='/login/')
def cerrar_sesion(request):
    logout(request)
    return render(request, 'core/login.html')

@login_required(login_url='/login/')
@permission_required('web.view_articulo',login_url='/login/')
def articulos(request):
    contexto={}
    articulos = Articulo.objects.all()
    categorias= Categoria.objects.all()
    contexto["items"]=articulos
    
    return render(request, 'admin/articulos.html',contexto)

@login_required(login_url='/login/')
@permission_required('web.add_articulo',login_url='/login/')
def agregar(request):
    contexto={}
    cant = Articulo.objects.all().count()
    print(cant)
    contexto["marcas"]= Marcas.objects.all()
    contexto["categorias"]= Categoria.objects.all()
    if request.POST:
        try:
            Codigo = cant+1
            Marca= request.POST.get('Marca')
            Cate= request.POST.get('Categoria')
            Nombre= request.POST.get('Nombre')
            Descripcion= request.POST.get('Descripcion')
            ima  = request.FILES.get("file")
            Precio=request.POST.get('Precio')
            Stock=request.POST.get('Stock')
            obj_marca= Marcas.objects.get(nombre=Marca)
            obj_categoria= Categoria.objects.get(nombre=Cate)
            art= Articulo(
                marca=obj_marca,
                categoria=obj_categoria,
                nombre=Nombre, 
                description=Descripcion, 
                precio=Precio,
                stock=Stock)
            if ima is not None:
                art.imagen= ima
            art.save()
            contexto["mensaje"]="Grabado"
        except BaseException as error:
            print(error)
            contexto["mensaje"]="problemas al grabar, revise sus datos "
    return render(request, 'admin/agregar.html',contexto)

@login_required(login_url='login/')
@permission_required('web.delete_articulo',login_url='/login/')
def eliminar(request,id):
    art = Articulo.objects.get(id=id)
    art.delete()
    return redirect('ART')

@login_required(login_url='login/')
@permission_required('web.view_articulo',login_url='/login/')
def modificar_buscar(request, id):
    art= Articulo.objects.get(id=id)
    contexto={}
    contexto["art"]=art
    print(art.description)
    contexto["items"] = Marcas.objects.all()
    contexto["categorias"] = Categoria.objects.all()
    return render(request,"admin/modificar.html",contexto)

@login_required(login_url='login/')
@permission_required('web.change_articulo',login_url='/login/')
def modificar(request):
    contexto={}
    contexto["marcas"]= Marcas.objects.all()
    contexto["categorias"]=  Categoria.objects.all()
    if request.POST:
        Codigo = request.POST.get('Codigo')
        Marca= request.POST.get('Marca')
        Cate=request.POST.get('Categoria')
        Nombre= request.POST.get('Nombre')
        Descripcion= request.POST.get('Descripcion')
        ima  = request.FILES.get("file")
        Precio=request.POST.get('Precio')
        Stock=request.POST.get('Stock')
        obj_marca= Marcas.objects.get(nombre=Marca)
        obj_cate= Categoria.objects.get(nombre=Cate)
        try:
            art= Articulo.objects.get(id=Codigo)
            art.categoria= obj_cate
            art.marca= obj_marca
            art.nombre= Nombre
            art.description= Descripcion
            art.precio=Precio
            art.stock= Stock
            if ima is not None:
                art.imagen = ima
            art.save()
            contexto["mensaje"]="Actualizado"
        except:
            contexto["mensaje"]="No se pudo actualizar"
    return render(request, 'admin/modificar.html',contexto)


def form_api(request):
    url="http://127.0.0.1:8000/API/lista_articulos"
    response = requests.get(url)
    # data = response.json().get([])
    print(response.json())
    data = response.json()
    context={
        'articulos': data
    }
    return render(request, 'admin/articulos_api.html',context)