from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = {
            'cliente',
            'cpf',
        }

    def save(self, commit=True):
        cliente         = Cliente()
        cliente.cliente = self.cleaned_data['cliente']
        cliente.cpf     = self.cleaned_data['cpf']

