from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Count
from .models import Resultado

@staff_member_required
def estadisticas_view(request):
    conteo = Resultado.objects.values('tipo_ingenieria').annotate(total=Count('tipo_ingenieria')).order_by('-total')
    
    etiquetas = [item['tipo_ingenieria'] for item in conteo]
    datos = [item['total'] for item in conteo]
    total_general = sum(datos)

    return render(request, 'admin/estadisticas.html', {
        'conteo': conteo,
        'etiquetas': etiquetas,
        'datos': datos,
        'total_general': total_general
    })