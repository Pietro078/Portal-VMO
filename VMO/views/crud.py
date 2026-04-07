from django.shortcuts import render, redirect, get_object_or_404
from ..models import Cliente, Registro
from ..forms import ClienteForm, RegistroForm

# ------------------------
# CLIENTE - CRUD
# ------------------------

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})


def cliente_create(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'cliente_form.html', {'form': form})


def cliente_update(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('cliente_list')
    return render(request, 'cliente_form.html', {'form': form})


def cliente_delete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'cliente_confirm_delete.html', {'cliente': cliente})


# ------------------------
# REGISTRO - CRUD
# ------------------------

def registro_list(request):
    registros = Registro.objects.select_related('ClienteUnidade').all()
    return render(request, 'registro_list.html', {'registros': registros})


def registro_create(request):
    form = RegistroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('registro_list')
    return render(request, 'registro_form.html', {'form': form})


def registro_update(request, id):
    registro = get_object_or_404(Registro, pk=id)
    form = RegistroForm(request.POST or None, instance=registro)
    if form.is_valid():
        form.save()
        return redirect('registro_list')
    return render(request, 'registro_form.html', {'form': form})


def registro_delete(request, id):
    registro = get_object_or_404(Registro, pk=id)
    if request.method == 'POST':
        registro.delete()
        return redirect('registro_list')
    return render(request, 'registro_confirm_delete.html', {'registro': registro})