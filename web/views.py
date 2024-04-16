from django.shortcuts import render

# Create your views here. (metodo en python que permita render de pag web)

def index(request): 
    return render(request, 'core\index.html')

def quienes_somos(request):
    return render(request, 'core\quienes_somos.html')

def admin_prod(request):
    return render(request, 'admin/admin_prod.html')