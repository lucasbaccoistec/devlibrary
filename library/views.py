from django.shortcuts import render, get_object_or_404
from .models import Recurso

def pagina_inicial(request):
    """Pagina principal: lista todos os recursos."""
    recursos = Recurso.objects.all()
    contexto = {
        'recursos': recursos,
        'total': recursos.count(),
    }
    return render(request, 'library/pagina_inicial.html', contexto)


def detalhe_recurso(request, recurso_id):
    """Pagina de detalhe de um unico recurso."""
    recurso = get_object_or_404(Recurso, pk=recurso_id)
    contexto = {
        'recurso': recurso,
    }
    return render(request, 'library/detalhe_recurso.html', contexto)