from django.contrib import admin
from .models import Tecnologia, Autor, Recurso


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'website')
    search_fields = ('nome',)


@admin.register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'tecnologia', 'autor', 'data_publicacao')
    list_filter = ('tipo', 'tecnologia')
    search_fields = ('titulo', 'descricao')