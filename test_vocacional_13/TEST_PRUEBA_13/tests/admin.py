from django.contrib import admin
from .models import TipoIngenieria, Pregunta, Opcion, Resultado
from django.urls import reverse

# Clase para administrar las opciones en línea dentro de la administración de preguntas
class OpcionInline(admin.TabularInline):
    model = Opcion  # Modelo que se va a mostrar como parte de la pregunta
    extra = 1  # Número de opciones vacías que se muestran por defecto

# Clase personalizada para la administración de preguntas
class PreguntaAdmin(admin.ModelAdmin):
    inlines = [OpcionInline]  # Incluir las opciones como parte de la administración de la pregunta
    
# Clase personalizada para la administración de resultados
class ResultadoAdmin(admin.ModelAdmin):
    # Definir los campos que se mostrarán en la lista de resultados
    list_display = ('usuario', 'get_email', 'tipo_ingenieria', 'fecha')
    # Permitir filtrado de resultados por tipo de ingeniería y fecha
    list_filter = ('tipo_ingenieria', 'fecha')
    # Hacer que los resultados se puedan buscar por nombre de usuario o tipo de ingeniería
    search_fields = ('usuario__username', 'tipo_ingenieria')

    # Método para obtener el correo electrónico del usuario
    def get_email(self, obj):
        return obj.usuario.email
    get_email.short_description = 'Email'  # Definir el nombre que se mostrará en la columna para el correo
    
    def changelist_view(self, request, extra_context=None):
        if extra_context is None:
            extra_context = {}
        # Pasamos la url de estadísticas para usarla en la plantilla
        extra_context['estadisticas_url'] = reverse('estadisticas')
        return super().changelist_view(request, extra_context=extra_context)

# Registro de los modelos en la interfaz de administración de Django
admin.site.register(TipoIngenieria)  # Registrar el modelo TipoIngenieria
admin.site.register(Pregunta, PreguntaAdmin)  # Registrar el modelo Pregunta con su configuración personalizada
admin.site.register(Resultado, ResultadoAdmin)  # Registrar el modelo Resultado con su configuración personalizada

