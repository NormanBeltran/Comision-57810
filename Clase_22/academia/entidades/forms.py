from django import forms 

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre de Curso")
    comision = forms.IntegerField(required=True)

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)   
    profesion = forms.CharField(max_length=50, required=True)