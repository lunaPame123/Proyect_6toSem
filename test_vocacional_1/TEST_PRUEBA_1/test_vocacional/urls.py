from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Vista para redirigir directamente al test vocacional
def home(request):
    return redirect('test_vocacional')  # Redirige automáticamente al test

urlpatterns = [
    path('admin/', admin.site.urls),       # Panel de administración
    path('test/', include('test_app.urls')),  # Ruta al test
    path('', home, name='home'),  # Redirige a test vocacional al acceder a la raíz
]

