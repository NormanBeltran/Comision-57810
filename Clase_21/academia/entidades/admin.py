from django.contrib import admin

# Register your models here.
from .models import *

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "comision")
    list_filter = ("nombre",)

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ("apellido", "nombre", "email", "profesion")

admin.site.register(Curso, CursoAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Estudiante)
admin.site.register(Entregable)
