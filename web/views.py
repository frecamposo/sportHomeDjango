from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate,login as login_aut,logout
from django.contrib.auth.decorators import login_required
from .models import Marcas, Articulo, UserProfile
# Create your views here. (metodo en python que permita render de pag web)

def index(request): 
    return render(request, 'core/index.html')

def quienes_somos(request):
    return render(request, 'core/quienes_somos.html')

@login_required(login_url='login/')
def futbol(request):
    return render(request, 'core/futbol.html')

@login_required(login_url='login/')
def basquetball(request):
    return render(request, 'core/basquetball.html')

@login_required(login_url='login/')
def natacion(request):
    return render(request, 'core/natacion.html')

@login_required(login_url='login/')
def tenis(request):
    return render(request, 'core/tenis.html')

@login_required(login_url='login/')
def voleyball(request):
    return render(request, 'core/voleyball.html')

@login_required(login_url='login/')
def sucursales(request):
    return render(request, 'core/sucursales.html')

@login_required(login_url='login/')
def producto(request):
    return render(request, 'core/producto.html')

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

@login_required(login_url='login/')
def registro(request):
    return render(request, 'core/registro.html')

def cerrar_sesion(request):
    logout(request)
    return render(request, 'core/login.html')

def articulos(request):
    contexto={}
    articulos = Articulo.objects.all()
    contexto["items"]=articulos
    
    return render(request, 'admin/articulos.html',contexto)

def agregar(request):
    return render(request, 'admin/agregar.html')