from django.db import models

# Modelo de negocio de la Aplicacion
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    class Meta:
        ordering = ["-nombre"]

    def __str__(self):
        return f"{self.nombre}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"    

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"
        ordering = ["nombre", "apellido"]

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre}"