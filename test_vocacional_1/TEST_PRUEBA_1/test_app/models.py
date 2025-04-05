from django.db import models

class Pregunta(models.Model):
    texto = models.CharField(max_length=200)

    def __str__(self):
        return self.texto

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    puntaje = models.IntegerField()

    def __str__(self):
        return f"{self.texto} (Puntaje: {self.puntaje})"

class Resultado(models.Model):
    descripcion = models.CharField(max_length=500)
    puntaje_minimo = models.IntegerField()

    def __str__(self):
        return f"Resultado: {self.descripcion} - Puntaje Mínimo: {self.puntaje_minimo}"

