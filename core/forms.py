from django import forms
from .models import Pedido
from .models import DetalhePedido

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['cliente'].widget.attrs['id'] = 'pedido-form-id'

class DetalhePedidoForm(forms.ModelForm):

    class Meta:
        model = DetalhePedido
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(DetalhePedidoForm, self).__init__(*args, **kwargs)
        self.fields['preco'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['preco'].widget.attrs['min'] = '0.01'
        self.fields['produto'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['quantidade'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['quantidade'].widget.attrs['min'] = '0'