from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    # cliente = forms.CharField(max_length=15)
    # CPF     = forms.CharField(max_length=11)

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


class UserCreationForm():
    pass