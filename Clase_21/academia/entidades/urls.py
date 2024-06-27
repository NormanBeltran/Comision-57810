from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),
    path('cursos/', cursos, name="cursos"),
    path('profesores/', profesores, name="profesores"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('entregables/', entregables, name="entregables"),

    path('acerca/', acerca, name="acerca"),

    #____ Formularios
    path('cursoForm/', cursoForm, name="cursoForm"),
    path('profesorForm/', profesorForm, name="profesorForm"),

    path('buscarCursos/', buscarCursos, name="buscarCursos"),
    path('encontrarCursos/', encontrarCursos, name="encontrarCursos"),
]