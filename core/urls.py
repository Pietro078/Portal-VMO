from django.contrib import admin
from django.urls import path
from VMO.views import view_cliente 
from VMO.views import view_registro 

urlpatterns = [
    path('cliente/',view_cliente.cliente, name="cliente"),
    path('cliente_delete/<int:id>/',view_cliente.cliente_delete, name="cliente_delete"),
    path('registro/',view_registro.registro, name="registro"),
    path('registro_create/',view_registro.registro_create, name="registro_create"),
    path('registro_update/',view_registro.registro_update, name="registro_update"),
   # path('', admin.site.urls),
] 