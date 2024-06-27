from django.shortcuts import render
from .models import *

# Copyright Norman Beltran

def home(request):
    return render(request, "entidades/index.html")

def cursos(request):
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)

def profesores(request):
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "entidades/profesores.html", contexto)

def estudiantes(request):
    contexto = {"estudiantes": Estudiante.objects.all()}
    return render(request, "entidades/estudiantes.html", contexto)

def entregables(request):
    contexto = {"entregables": Entregable.objects.all()}
    return render(request, "entidades/entregables.html", contexto)

def acerca(request):
    return render(request, "entidades/acerca.html")