from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre de Curso")
    comision = forms.IntegerField(required=True)

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)   
    profesion = forms.CharField(max_length=50, required=True)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]