
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import EditableContent


def index(request):
    objetos = EditableContent.objects.all()
    return render(request, 'index.html', {'objetos': objetos})


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
    # Obtiene un solo objeto basado en el ID (pk)
    objeto = get_object_or_404(EditableContent, pk=1)
    return render(request, 'detalles_ahorrar.html',  {'objeto': objeto})

def detalles_inversion(request):
    objeto = get_object_or_404(EditableContent, pk=2)
    return render(request, 'detalles_inversion.html',  {'objeto': objeto})

def detalles_deuda(request):
    objeto = get_object_or_404(EditableContent, pk=3)
    return render(request, 'detalles_deuda.html',  {'objeto': objeto})

def detalles_planificacion(request):
    objeto = get_object_or_404(EditableContent, pk=5)
    return render(request, 'detalles_planificacion.html',  {'objeto': objeto})

def detalles_jubilacion(request):
    objeto = get_object_or_404(EditableContent, pk=6)
    return render(request, 'detalles_jubilacion.html',  {'objeto': objeto})


def detalles_ahorro_inteligente(request):
    objeto = get_object_or_404(EditableContent, pk=4)
    return render(request, 'detalles_ahorro_inteligente.html',  {'objeto': objeto})
