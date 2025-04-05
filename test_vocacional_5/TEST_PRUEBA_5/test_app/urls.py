from django.urls import path
from .views import test_vocacional, registrar_usuario, login_usuario, logout_usuario
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('test/', test_vocacional, name='test_vocacional'),
    path('registro/', registrar_usuario, name='registro'),
    path('login/', login_usuario, name='login'),
    path('logout/', logout_usuario, name='logout'),
]
