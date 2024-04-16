from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login as login_aut,logout
from django.contrib.auth.decorators import login_required,permission_required
from .models import Marcas, Articulo, UserProfile
# Create your views here. (metodo en python que permita render de pag web)

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
    return render(request, 'core/tenis.html')

@login_required(login_url='/login/')
def voleyball(request):
    return render(request, 'core/voleyball.html')

@login_required(login_url='/login/')
def sucursales(request):
    return render(request, 'core/sucursales.html')

@login_required(login_url='/login/')
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
    contexto["items"]=articulos
    
    return render(request, 'admin/articulos.html',contexto)

@login_required(login_url='/login/')
@permission_required('web.add_articulo',login_url='/login/')
def agregar(request):
    contexto={}
    contexto["marcas"]= Marcas.objects.all()
    if request.POST:
        try:
            Codigo = request.POST.get('Codigo')
            Marca= request.POST.get('Marca')
            Nombre= request.POST.get('Nombre')
            Descripcion= request.POST.get('Descripcion')
            Precio=request.POST.get('Precio')
            Stock=request.POST.get('Stock')
            obj_marca= Marcas.objects.get(nombre=Marca)
            art= Articulo(Codigo,obj_marca,Nombre, Descripcion, Precio,Stock)
            art.save()
            contexto["mensaje"]="Grabado"
        except:
            contexto["mensaje"]="problemas al grabar, revise sus datos"
    return render(request, 'admin/agregar.html',contexto)

@login_required(login_url='login/')
@permission_required('web.delete_articulo',login_url='/login/')
def eliminar(request,id):
    art = Articulo.objects.get(codigo=id)
    art.delete()
    return redirect('ART')

@login_required(login_url='login/')
@permission_required('web.view_articulo',login_url='/login/')
def modificar_buscar(request, id):
    art= Articulo.objects.get(codigo=id)
    contexto={}
    contexto["art"]=art
    print(art.description)
    contexto["items"] = Marcas.objects.all()
    return render(request,"admin/modificar.html",contexto)

@login_required(login_url='login/')
@permission_required('web.change_articulo',login_url='/login/')
def modificar(request):
    contexto={}
    contexto["marcas"]= Marcas.objects.all()
    if request.POST:
        Codigo = request.POST.get('Codigo')
        Marca= request.POST.get('Marca')
        Nombre= request.POST.get('Nombre')
        Descripcion= request.POST.get('Descripcion')
        Precio=request.POST.get('Precio')
        Stock=request.POST.get('Stock')
        obj_marca= Marcas.objects.get(nombre=Marca)
        
        try:
            art= Articulo.objects.get(codigo=Codigo)
            art.marca= obj_marca
            art.nombre= Nombre
            art.description= Descripcion
            art.precio=Precio
            art.stock= Stock
            art.save()
            contexto["mensaje"]="Actualizado"
        except:
            contexto["mensaje"]="No se pudo actualizar"
    return render(request, 'admin/modificar.html',contexto)
