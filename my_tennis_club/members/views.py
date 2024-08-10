
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        # Manejar autenticación
        pass
    return render(request, 'login.html')

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