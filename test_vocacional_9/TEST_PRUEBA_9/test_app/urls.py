
from django.urls import path
from .views import test_vocacional, registrar_usuario, login_usuario, logout_usuario

urlpatterns = [
    path('', login_usuario, name='login'),
    path('registro/', registrar_usuario, name='registro'),
    path('test/', test_vocacional, name='test_vocacional'),
    path('logout/', logout_usuario, name='logout'),
]
