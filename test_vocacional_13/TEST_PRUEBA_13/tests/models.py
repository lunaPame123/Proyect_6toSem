from django.db import models
from django.contrib.auth.models import User

# Modelo que representa los diferentes tipos de ingeniería
class TipoIngenieria(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del tipo de ingeniería (ej. "Ingeniería de Software")

    def __str__(self):
        return self.nombre  # Devuelve el nombre del tipo de ingeniería para representarlo en las vistas

# Modelo que representa una pregunta en el test vocacional
class Pregunta(models.Model):
    texto = models.TextField()  # Texto de la pregunta

    def __str__(self):
        return self.texto  # Devuelve el texto de la pregunta como representación en las vistas

# Modelo que representa una opción para una pregunta
class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')  # Relación con la pregunta
    texto = models.CharField(max_length=255)  # Texto de la opción
    tipo_ingenieria = models.ForeignKey(TipoIngenieria, on_delete=models.SET_NULL, null=True)  # Relación con el tipo de ingeniería

    def __str__(self):
        # Devuelve una cadena con el texto de la opción y el tipo de ingeniería, si existe
        return f"{self.texto} → {self.tipo_ingenieria.nombre if self.tipo_ingenieria else 'Ninguna'}"

# Modelo que representa los resultados del test de un usuario
class Resultado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario que realizó el test
    tipo_ingenieria = models.CharField(max_length=100)  # Tipo de ingeniería basado en el resultado
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha en que se registró el resultado, automáticamente asignada al crear

    def __str__(self):
        # Devuelve una cadena con el nombre del usuario, el tipo de ingeniería y la fecha en formato legible
        return f"{self.usuario.username} - {self.tipo_ingenieria} ({self.fecha.strftime('%d/%m/%Y %H:%M')})"
