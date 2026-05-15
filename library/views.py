from django.shortcuts import render, get_object_or_404
from .models import Recurso, Tecnologia, Autor


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


def recursos_por_tecnologia(request, tecnologia_id):
    """Lista todos os recursos de uma tecnologia."""
    tecnologia = get_object_or_404(Tecnologia, pk=tecnologia_id)
    recursos = tecnologia.recursos.all()
    contexto = {
        'recursos': recursos,
        'titulo_pagina': f'Recursos de {tecnologia.nome}',
        'subtitulo': tecnologia.descricao,
        'total': recursos.count(),
    }
    return render(request, 'library/lista_recursos.html', contexto)


def recursos_por_autor(request, autor_id):
    """Lista todos os recursos de um autor."""
    autor = get_object_or_404(Autor, pk=autor_id)
    recursos = autor.recursos.all()
    contexto = {
        'recursos': recursos,
        'titulo_pagina': f'Recursos de {autor.nome}',
        'subtitulo': autor.bio,
        'total': recursos.count(),
    }
    return render(request, 'library/lista_recursos.html', contexto)