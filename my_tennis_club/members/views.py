
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        # Manejar autenticación
        pass
    return render(request, 'login.html')

