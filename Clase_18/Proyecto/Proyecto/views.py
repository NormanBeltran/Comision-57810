from django.template import Template, Context, loader
from django.http import HttpResponse

import datetime, random
from aplicacion.models import *

def saludar(request):
    saludo = "Bienvenidos a la Comision 57810 - Clases de Django"
    return HttpResponse(saludo)

def bienvenido(request, nombre, apellido):
    saludo = f"Te damos la bienvenida a la Comision 57810 {apellido}, {nombre}"
    return HttpResponse(saludo)

def bienvenido_html(request, nombre, apellido):
    hoy = datetime.datetime.now()
    saludo = f"""
    <html>
    <h1>Bienvenidos al Curso de Django!</h1>
    <h2>Te damos la bienvenida {apellido}, {nombre}</h2>
    <h3>Hoy es {hoy}</h3>
    </html>
    """
    return HttpResponse(saludo)

def bienvenido_tpl(request):
    with open("C:/CoderHouse/57810/Clase_18/Proyecto/Proyecto/plantillas/bienvenido.html") as miHtml:
        plantilla = Template(miHtml.read())
        contexto  = Context()
        saludo = plantilla.render(contexto)

    return HttpResponse(saludo)

#_________________________________________________________
def bienvenido_tpl2(request):
    hoy = datetime.datetime.now()
    nombre = "Amadeus"
    apellido = "Mozart"
    notas = [3,8,9,6,10,4]
    contexto = {"nombre": nombre, "apellido": apellido, "hoy": hoy,
                "notas": notas}
    
    plantilla = loader.get_template("bienvenido_tpl.html")
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)

def nuevo_curso(request):
    nro_comision = random.randint(1000, 200000)
    nombre_curso = "Python [" + str(nro_comision) + "]"
    curso = Curso(nombre=nombre_curso, comision=nro_comision)
    curso.save()
    respuesta = f"<html><h1>Se guardo {nombre_curso} y comision {nro_comision}</h1></html>"
    return HttpResponse(respuesta)