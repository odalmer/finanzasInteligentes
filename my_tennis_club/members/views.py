from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import EditableContent
from .forms import EditableContentForm
from django.shortcuts import render, redirect

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

def home_view(request):
    return render(request, 'home.html')

def privacy_policy_view(request):
    return render(request, 'privacy_policy.html')

def contact_view(request):
    return render(request, 'contact.html')

def news_view(request):
    return render(request, 'news.html')

def list_view(request):
    return render(request, 'list.html')

def login_view(request):
    return render(request, 'login.html')

def profile_view(request):
    return render(request, 'profile.html', {})

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = EditableContentForm(request.POST, request.FILES)
        if form.is_valid():
            editable_content = form.save(commit=False)
            editable_content.created_by = request.user
            editable_content.save()
            return redirect('profile')
    else:
        form = EditableContentForm()

    return render(request, 'profile.html', {'form': form})


