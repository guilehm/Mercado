from django import forms
from .models import Pedido
from .models import DetalhePedido

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = '__all__'


class DetalhePedidoForm(forms.ModelForm):

    class Meta:
        model = DetalhePedido
        fields = '__all__'