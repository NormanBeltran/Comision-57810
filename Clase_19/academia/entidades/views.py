from django.shortcuts import render
from .models import *

# Copyright Norman Beltran

def home(request):
    return render(request, "entidades/index.html")

def cursos(request):
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)

def profesores(request):
    return render(request, "entidades/profesores.html")

def estudiantes(request):
    return render(request, "entidades/estudiantes.html")

def entregables(request):
    return render(request, "entidades/entregables.html")