from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pregunta, Opcion, Resultado, PerfilUsuario

def registrar_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
        else:
            user = User.objects.create_user(username=username, password=password)
            PerfilUsuario.objects.create(usuario=user)  # Crear perfil de usuario
            login(request, user)  
            return redirect('test_vocacional')

    return render(request, 'test_app/registro.html')

def login_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('test_vocacional')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, 'test_app/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('login')

@login_required
def test_vocacional(request):
    preguntas = Pregunta.objects.all()
    tiempo_limite = 300  # Tiempo límite en segundos (5 minutos)

    if request.method == "POST":
        puntaje_total = 0

        for pregunta in preguntas:
            opcion_id = request.POST.get(f"pregunta_{pregunta.id}")
            if opcion_id:
                try:
                    opcion = Opcion.objects.get(id=opcion_id)
                    puntaje_total += opcion.puntaje
                except Opcion.DoesNotExist:
                    continue

        resultado = Resultado.objects.filter(puntaje_minimo__lte=puntaje_total).order_by('-puntaje_minimo').first()

        if request.user.is_authenticated:
            perfil, created = PerfilUsuario.objects.get_or_create(usuario=request.user)
            perfil.resultado_test = resultado
            perfil.puntaje_obtenido = puntaje_total
            perfil.save()

        return render(request, 'test_app/resultado.html', {'resultado': resultado, 'puntaje_total': puntaje_total})

    return render(request, 'test_app/test.html', {'preguntas': preguntas, 'tiempo_limite': tiempo_limite})

