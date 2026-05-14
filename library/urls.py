from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('recurso/<int:recurso_id>/', views.detalhe_recurso, name='detalhe_recurso'),
]