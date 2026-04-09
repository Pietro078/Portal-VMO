from django.db import models

class Cliente(models.Model):
    ID_cliente = models.AutoField(primary_key=True)
    Cliente = models.CharField(max_length=150)
    Unidade = models.CharField(max_length=100, unique=True)
    UF = models.CharField(max_length=9)

    def __str__(self):
        return f"{self.Cliente} - {self.Unidade} ({self.UF})"

class Registro(models.Model):
    ID_registro = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='registros'
    )
    km_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    km_final = models.DecimalField(max_digits=10, decimal_places=2)
    responsavel = models.CharField(max_length=100)

    def __str__(self):
        return f"Registro {self.ID_registro}"