from django.urls import path
from VMO.views import view_crud

urlpatterns = [
    # CLIENTES
    path('clientes/', view_crud.cliente_list, name='cliente_list'),
    path('clientes/salvar/', view_crud.cliente_save, name='cliente_create'),
    path('clientes/salvar/<int:id>/', view_crud.cliente_save, name='cliente_update'),
    path('clientes/deletar/<int:id>/', view_crud.cliente_delete, name='cliente_delete'),

    # REGISTROS
    path('registros/', view_crud.registro_list, name='registro_list'),
    path('registros/salvar/', view_crud.registro_save, name='registro_create'),
    path('registros/salvar/<int:id>/', view_crud.registro_save, name='registro_update'),
    path('registros/deletar/<int:id>/', view_crud.registro_delete, name='registro_delete'),
]