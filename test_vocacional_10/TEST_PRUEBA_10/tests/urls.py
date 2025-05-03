from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),          # Página principal
    path('register/', views.register_view, name='register'),
    path('home/', views.home, name='home'),
    path('empezar-test/', views.test_view, name='empezar_test'),
    path('historial/', views.historial_view, name='historial'),
    path('logout/', views.logout_view, name='logout'),  # Página de cierre de sesión
]
