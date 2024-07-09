from django.urls import path, include
from entidades.views import *

from django.contrib.auth.views import LogoutView

# Copyright Norman Beltran

urlpatterns = [
    path('', home, name="home"),

    path('entregables/', entregables, name="entregables"),

    path('acerca/', acerca, name="acerca"),

    #____ Cursos
    path('cursos/', cursos, name="cursos"),
    path('cursoForm/', cursoForm, name="cursoForm"),
    path('cursoUpdate/<id_curso>/', cursoUpdate, name="cursoUpdate"),
    path('cursoDelete/<id_curso>/', cursoDelete, name="cursoDelete"),

    #____ Profesores
    path('profesores/', profesores, name="profesores"),    
    path('profesorForm/', profesorForm, name="profesorForm"),
    path('profesorUpdate/<id_profesor>/', profesorUpdate, name="profesorUpdate"),
    path('profesorDelete/<id_profesor>/', profesorDelete, name="profesorDelete"),

    #____ Estudiantes
    path('estudiantes/', EstudianteList.as_view(), name="estudiantes"),    
    path('estudianteCreate/', EstudianteCreate.as_view(), name="estudianteCreate"), 
    path('estudianteUpdate/<int:pk>/', EstudianteUpdate.as_view(), name="estudianteUpdate"), 
    path('estudianteDelete/<int:pk>/', EstudianteDelete.as_view(), name="estudianteDelete"), 


    #___ Buscar
    path('buscarCursos/', buscarCursos, name="buscarCursos"),
    path('encontrarCursos/', encontrarCursos, name="encontrarCursos"),

    #___ Login / Logout / Registration
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),

    #___ Edición de Perfil / Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]