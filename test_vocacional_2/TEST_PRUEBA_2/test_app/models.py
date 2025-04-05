from django.contrib.auth.models import User
from django.db import models

class Pregunta(models.Model):
    texto = models.CharField(max_length=255)

    def __str__(self):
        return self.texto

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=255)
    puntaje = models.IntegerField()

    def __str__(self):
        return self.texto

class Resultado(models.Model):
    descripcion = models.TextField()
    puntaje_minimo = models.IntegerField()

    def __str__(self):
        return self.descripcion

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    resultado_test = models.ForeignKey(Resultado, null=True, blank=True, on_delete=models.SET_NULL)
    fecha_realizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username

