from django.contrib import admin
from .models import Pregunta, Opcion, Resultado, PerfilUsuario

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'resultado_test', 'puntaje_obtenido', 'fecha_realizacion')


# Creamos un Inline para mostrar las Opciones dentro de la Pregunta
class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 3  # Puedes ajustar la cantidad de opciones vacías que aparecerán por defecto

# Ahora personalizamos la vista del admin para la Pregunta
class PreguntaAdmin(admin.ModelAdmin):
    inlines = [OpcionInline]

# Registramos los modelos
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Resultado)