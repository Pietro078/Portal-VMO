from django.urls import path
from VMO.views import view_crud

urlpatterns = [
    # CLIENTES
    path('', view_crud.cliente, name='cliente_list'),

]           