from django.db import models

# Modelo de negocio de la Aplicacion
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()