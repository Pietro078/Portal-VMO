from django import forms
from .models import Cliente, Registro

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['ClienteUnidade', 'UF']


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ['ClienteUnidade', 'km_inicial', 'km_final', 'responsavel']