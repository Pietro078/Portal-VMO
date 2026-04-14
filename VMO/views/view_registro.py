from django.shortcuts import render, redirect, get_object_or_404
from ..models import Cliente, Registro
from Assets import assets

def registro(request):
    if request.method == "GET":
        return render(
            request, "registro.html", {
            "registro": Registro.objects.all(), 
            "cliente":Cliente.objects.all()
            }
    )
    
def registro_create(request):
    if request.method == "GET":
        return render(request, "registro.html", {"registros": Registro.objects.all()})

def registro_update(request):
    if request.method == "GET":
        return render(request, "registro.html", {"registros": Registro.objects.all()})