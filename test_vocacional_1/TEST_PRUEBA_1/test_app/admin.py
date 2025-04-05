from django.contrib import admin
from .models import Pregunta, Opcion, Resultado

admin.site.register(Pregunta)
admin.site.register(Opcion)
admin.site.register(Resultado)
