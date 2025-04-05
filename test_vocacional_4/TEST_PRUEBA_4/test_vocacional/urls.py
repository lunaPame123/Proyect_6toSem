from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('login')  # Redirige a la página de login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('test_app.urls')),
    path('', home, name='home'),
]
