from django.db import models

class Cliente(models.Model):
    ID_uni = models.AutoField(primary_key=True)
    ClienteUnidade = models.CharField(max_length=150)
    UF = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.ClienteUnidade} - {self.UF}"


class Registro(models.Model):
    ID_registro = models.AutoField(primary_key=True)
    ClienteUnidade = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    km_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    km_final = models.DecimalField(max_digits=10, decimal_places=2)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return f"Registro {self.ID_registro} - {self.ClienteUnidade}"