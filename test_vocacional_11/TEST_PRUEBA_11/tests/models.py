from django.db import models
from django.contrib.auth.models import User

class TipoIngenieria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Pregunta(models.Model):
    texto = models.TextField()

    def __str__(self):
        return self.texto

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto = models.CharField(max_length=255)
    tipo_ingenieria = models.ForeignKey(TipoIngenieria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.texto} → {self.tipo_ingenieria.nombre if self.tipo_ingenieria else 'Ninguna'}"

class Resultado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_ingenieria = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.tipo_ingenieria} ({self.fecha.strftime('%d/%m/%Y %H:%M')})"