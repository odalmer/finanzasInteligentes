from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    datos = Member.objects.all()
    template = loader.get_template('myfirst.html')
    context = {
        'datos': datos,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())