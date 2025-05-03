from django.contrib import admin
from .models import TipoIngenieria, Pregunta, Opcion

class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 1  # Cuántas opciones vacías se muestran por defecto

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [OpcionInline]

admin.site.register(TipoIngenieria)
admin.site.register(Pregunta, PreguntaAdmin)
