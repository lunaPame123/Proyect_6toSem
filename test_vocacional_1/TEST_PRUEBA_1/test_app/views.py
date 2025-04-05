from django.shortcuts import render
from .models import Pregunta, Opcion, Resultado

def test_vocacional(request):
    preguntas = Pregunta.objects.all()

    if request.method == "POST":
        puntaje_total = 0
        puntaje_obtenido = 0  # Esta es la variable para almacenar el puntaje obtenido por el usuario

        # Iterar sobre las preguntas para sumar los puntajes
        for pregunta in preguntas:
            opcion_id = request.POST.get(f"pregunta_{pregunta.id}")
            if opcion_id:
                try:
                    opcion = Opcion.objects.get(id=opcion_id)  # Buscar la opción seleccionada
                    puntaje_obtenido += opcion.puntaje  # Sumamos el puntaje de la opción seleccionada
                except Opcion.DoesNotExist:
                    print(f"Opción con ID {opcion_id} no existe.")  # Para depuración
                    continue

        # Buscar el resultado basado en el puntaje obtenido
        resultado = Resultado.objects.filter(puntaje_minimo__lte=puntaje_obtenido).order_by('-puntaje_minimo').first()

        # Pasamos tanto el puntaje obtenido como el puntaje total al template
        return render(request, 'test_app/resultado.html', {'resultado': resultado, 'puntaje_obtenido': puntaje_obtenido})

    # Si es un GET, mostramos las preguntas del test
    return render(request, 'test_app/test.html', {'preguntas': preguntas})

