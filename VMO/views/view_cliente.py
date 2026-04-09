from django.shortcuts import render, redirect, get_object_or_404
from ..models import Cliente, Registro
from Assets import assets

def cliente(request):
    
    if request.method == "GET":
        return render(request, "cliente.html", {"cliente":Cliente.objects.all()})

    if request.method == "POST":
        id_cliente = request.POST.get("id")
        
        clientee = assets.remover_acentos((request.POST.get("cliente") or "").strip().upper())
        unidade = assets.remover_acentos((request.POST.get("unidade") or "").strip().upper())
        codigo_unidade = assets.remover_acentos((request.POST.get("codigo_unidade") or "").strip().upper())
        uf = assets.remover_acentos((request.POST.get("uf") or "").strip().upper())
        
        #! Validação de campos vazios
        lista = [clientee, unidade, codigo_unidade,uf]
        for a in lista:
            if a == "":
                return render(request, "cliente.html", {"cliente":Cliente.objects.all(), "erro": "Valor vazio constando"})
        
        
        
        #! 🔥 SE FOR EDIÇÃO
        if id_cliente:
            cliente = Cliente.objects.get(ID_cliente=id_cliente)

            cliente.Cliente = clientee
            cliente.Unidade = unidade
            cliente.Codigo_unidade = codigo_unidade
            cliente.UF = uf
            cliente.save()

        else:
            if Cliente.objects.filter(Codigo_unidade = codigo_unidade) or Cliente.objects.filter(Unidade = unidade) :
                return render(request, "cliente.html", {"cliente":Cliente.objects.all(), "erro": "Unidade ou Código unidade já existem no banco"})
        #! 🔥 CRIAÇÃO
            Cliente.objects.create(
                Cliente=clientee,
                Unidade=unidade,
                Codigo_unidade=codigo_unidade,
                UF=uf
            )

        return redirect("cliente")

def cliente_delete(request, id):
    if request.method == "POST":
        try:
            Cliente.objects.filter(ID_cliente=id).delete()
            return redirect("cliente")
        except:
            return print("ola mundo")