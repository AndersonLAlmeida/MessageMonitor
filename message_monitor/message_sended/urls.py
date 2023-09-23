from django.urls import path
from .views import adicionar_registro, listar_registros

urlpatterns = [

    path('adicionar/', adicionar_registro, name='adicionar_registro'),
    path('listar/', listar_registros, name='listar_registros'),
    # Outras URLs
]