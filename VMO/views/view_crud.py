from django.shortcuts import render, redirect, get_object_or_404
from ..models import Cliente, Registro

def cliente(request):
    if request.method == "GET":
        return render(request, "cliente.html", {"TB_cliente":Cliente.objects.all()})

    if request.method == "POST":
        cliente = request.POST.get("cliente")
        unidade = request.POST.get("unidade")
        uf = request.POST.get("uf")

        print(cliente, "====", unidade, "====", uf)

        #! VALIDAÇÃO: verificar se já existe
        if Cliente.objects.filter(Unidade=unidade).exists():
            return render(request, "cliente.html", {
                "erro": "Já existe uma unidade cadastrada com esse nome!"
            })

        #! Se não existir, salva
        Cliente.objects.create(
            Cliente=cliente,
            Unidade=unidade,
            UF=uf
        )

        return redirect("cliente_list")

    return render(request, "cliente.html")
