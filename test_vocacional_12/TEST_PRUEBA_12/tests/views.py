from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Pregunta, Opcion
from collections import Counter
from .models import Resultado  # importar el nuevo modelo

@login_required
def test_view(request):
    if request.method == 'POST':
        respuestas = request.POST
        conteo = Counter()

        for key in respuestas:
            if key.startswith('pregunta_'):
                opcion_id = respuestas[key]
                try:
                    opcion = Opcion.objects.get(id=opcion_id)
                    if opcion.tipo_ingenieria:
                        conteo[opcion.tipo_ingenieria.nombre] += 1
                except Opcion.DoesNotExist:
                    pass

        if conteo:
            resultado = conteo.most_common(1)[0][0]
            Resultado.objects.create(usuario=request.user, tipo_ingenieria=resultado)  # 👈 Guarda el resultado
        else:
            resultado = "No se pudo determinar un resultado."
            
        # Guardar el resultado en la base de datos
        Resultado.objects.create(
            usuario=request.user,
            tipo_ingenieria=resultado
        )

        return render(request, 'tests/resultado.html', {'resultado': resultado})

    preguntas = Pregunta.objects.prefetch_related('opciones').all()
    return render(request, 'tests/test.html', {'preguntas': preguntas})


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')  # Obtiene el email del formulario

        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuario ya existente. Por favor, inicia sesión.')
            return redirect('login')
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # No guarda aún en la base de datos
            user.email = email              # Asigna el email
            user.save()                     # Ahora sí guarda el usuario con email
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirigir a login después de registrar
        else:
            # Mostrar errores del formulario LIMPIOS
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
            messages.error(request, 'Error en el registro. Verifica los datos ingresados.')
    else:
        form = UserCreationForm()
    
    return render(request, 'tests/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {username} 🎉')
            return redirect('home')  # Redirigir a la página principal después de login exitoso
        else:
            # Verificar si el usuario existe
            if not User.objects.filter(username=username).exists():
                messages.error(request, 'Usuario no encontrado. Por favor, regístrese.')
                return redirect('register')
            else:
                messages.error(request, 'Contraseña incorrecta. Inténtalo de nuevo.')
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'tests/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'tests/home.html', {'user': request.user})

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión correctamente.')  # Mensaje de logout
    return redirect('login')  # Redirigir al inicio de sesión después de cerrar sesión

@login_required
def historial_view(request):
    historial = Resultado.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'tests/historial.html', {'historial': historial})

