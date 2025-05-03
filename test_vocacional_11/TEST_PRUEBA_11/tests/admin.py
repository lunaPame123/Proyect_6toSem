from django.contrib import admin
from .models import TipoIngenieria, Pregunta, Opcion, Resultado

class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 1  # Cuántas opciones vacías se muestran por defecto

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [OpcionInline]
    
class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_ingenieria', 'fecha')
    list_filter = ('tipo_ingenieria', 'fecha')
    search_fields = ('usuario__username', 'tipo_ingenieria')

admin.site.register(TipoIngenieria)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Resultado, ResultadoAdmin)

