
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print(request.POST)
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('/admin/')
        
def detalles_ahorrar(request):
    return render(request, 'detalles_ahorrar.html')

def detalles_inversion(request):
    return render(request, 'detalles_inversion.html')

def detalles_deuda(request):
    return render(request, 'detalles_deuda.html')

def detalles_planificacion(request):
    return render(request, 'detalles_planificacion.html')

def detalles_jubilacion(request):
    return render(request, 'detalles_jubilacion.html')

def detalles_ahorro_inteligente(request):
    return render(request, 'detalles_ahorro_inteligente.html')
