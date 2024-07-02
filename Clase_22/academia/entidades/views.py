from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *

from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

# Copyright Norman Beltran

def home(request):
    return render(request, "entidades/index.html")

def estudiantes(request):
    contexto = {"estudiantes": Estudiante.objects.all()}
    return render(request, "entidades/estudiantes.html", contexto)

def entregables(request):
    contexto = {"entregables": Entregable.objects.all()}
    return render(request, "entidades/entregables.html", contexto)

def acerca(request):
    return render(request, "entidades/acerca.html")

#___ Cursos
def cursos(request):
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)

def cursoForm(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_nombre = miForm.cleaned_data.get("nombre")
            curso_comision = miForm.cleaned_data.get("comision")
            curso = Curso(nombre=curso_nombre, comision=curso_comision)
            curso.save()
            contexto = {"cursos": Curso.objects.all() }
            return render(request, "entidades/cursos.html", contexto)
    else:
        miForm = CursoForm()
    
    return render(request, "entidades/cursoForm.html", {"form": miForm})

def cursoUpdate(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso.nombre = miForm.cleaned_data.get("nombre")
            curso.comision = miForm.cleaned_data.get("comision")
            curso.save()
            contexto = {"cursos": Curso.objects.all() }
            return render(request, "entidades/cursos.html", contexto)       
    else:
        miForm = CursoForm(initial={"nombre": curso.nombre, "comision": curso.comision}) 
    
    return render(request, "entidades/cursoForm.html", {"form": miForm})

def cursoDelete(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    curso.delete()
    contexto = {"cursos": Curso.objects.all() }
    return render(request, "entidades/cursos.html", contexto)     

#___ Profesores
def profesores(request):
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "entidades/profesores.html", contexto)

def profesorForm(request):
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            profe_nombre = miForm.cleaned_data.get("nombre")
            profe_apellido = miForm.cleaned_data.get("apellido")
            profe_email = miForm.cleaned_data.get("email")
            profe_profesion = miForm.cleaned_data.get("profesion")

            profesor = Profesor(nombre=profe_nombre, 
                          apellido=profe_apellido,
                          email=profe_email,
                          profesion=profe_profesion)
            profesor.save()
            contexto = {"profesores": Profesor.objects.all() }
            return render(request, "entidades/profesores.html", contexto)
    else:
        miForm = ProfesorForm()
    
    return render(request, "entidades/profesorForm.html", {"form": miForm})

def profesorUpdate(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            profesor.nombre = miForm.cleaned_data.get("nombre")
            profesor.apellido = miForm.cleaned_data.get("apellido")
            profesor.email = miForm.cleaned_data.get("email")
            profesor.profesion = miForm.cleaned_data.get("profesion")
            profesor.save()
            contexto = {"profesores": Profesor.objects.all() }
            return render(request, "entidades/profesores.html", contexto)
    else:
        miForm = ProfesorForm(initial={"nombre": profesor.nombre,
                                       "apellido": profesor.apellido,
                                       "email": profesor.email,
                                       "profesion": profesor.profesion})
    
    return render(request, "entidades/profesorForm.html", {"form": miForm})

def profesorDelete(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    contexto = {"profesores": Profesor.objects.all() }
    return render(request, "entidades/profesores.html", contexto)     

#___ Estudiante
class EstudianteList(ListView):
    model = Estudiante

class EstudianteCreate(CreateView):
    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("estudiantes")

class EstudianteUpdate(UpdateView):
    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("estudiantes")

class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy("estudiantes")

#___ Buscar
def buscarCursos(request):
    return render(request, "entidades/buscar.html")

def encontrarCursos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {'cursos': cursos}    
    else:
        contexto = {'cursos': Curso.objects.all()}
        
    return render(request, "entidades/cursos.html", contexto)