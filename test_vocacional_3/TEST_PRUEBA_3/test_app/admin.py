from django.contrib import admin
from .models import Pregunta, Opcion, Resultado, PerfilUsuario

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'resultado_test', 'puntaje_obtenido', 'fecha_realizacion')

admin.site.register(Pregunta)
admin.site.register(Opcion)
admin.site.register(Resultado)
