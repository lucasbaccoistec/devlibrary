from django.shortcuts import render
from .models import Recurso


def pagina_inicial(request):
    """Pagina principal: lista todos os recursos."""
    recursos = Recurso.objects.all()
    contexto = {
        'recursos': recursos,
        'total': recursos.count(),
    }
    return render(request, 'library/pagina_inicial.html', contexto)