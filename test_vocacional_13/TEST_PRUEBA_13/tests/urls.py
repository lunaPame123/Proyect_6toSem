from django.urls import path
from . import views
from .admin_views import estadisticas_view

urlpatterns = [
    # Ruta para la página de inicio (login), que muestra el formulario de inicio de sesión
    path('', views.login_view, name='login'),          # Página principal de login
    
    # Ruta para la página de registro, donde los usuarios pueden crear una cuenta
    path('register/', views.register_view, name='register'),
    
    # Ruta para la página principal del usuario, después de haber iniciado sesión
    path('home/', views.home, name='home'),
    
    # Ruta para iniciar el test vocacional
    path('empezar-test/', views.test_view, name='empezar_test'),
    
    # Ruta para ver el historial de resultados del usuario
    path('historial/', views.historial_view, name='historial'),
    
    # Ruta para cerrar la sesión del usuario
    path('logout/', views.logout_view, name='logout'),  # Página de cierre de sesión
    
    path('estadisticas/', estadisticas_view, name='estadisticas'),
]
