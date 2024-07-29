from django.db import models
from django import forms

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.categoria

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_de_publicacion = models.DateField()

    def __str__(self):
        return self.titulo