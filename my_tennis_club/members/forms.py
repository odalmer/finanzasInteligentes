from django import forms
from .models import EditableContent
from django.contrib.auth.forms import AuthenticationForm

class EditableContentForm(forms.ModelForm):
    class Meta:
        model = EditableContent
        fields = ['title', 'content', 'image']

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    