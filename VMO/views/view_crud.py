from django.shortcuts import render, redirect, get_object_or_404
from ..models import Cliente, Registro

def cliente(request):
    if request.method == "POST":
        # Aqui você pega os dados enviados pelo formulário
        nome = request.POST.get("nome")
        email = request.POST.get("email")

        # Exemplo: cria um Cliente
        novo_cliente = Cliente.objects.create(
            nome=nome,
            email=email
        )

        # Depois de salvar, é comum redirecionar para evitar salvar duplicado no F5
        return redirect("cliente_lista")  # ou a página que você quiser

    # Se não for POST, então é GET (abrir a página/form)
    clientes = Cliente.objects.all()
    return render(request, "cliente.html", {"clientes": clientes})
