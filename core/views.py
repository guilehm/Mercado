from django.shortcuts import render
from .models import Produto
from .models import Pedido
from .forms import ClienteForm

# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos':produtos,
    }
    return render(request, 'core/produtos.html', context)

def pedidos(request):
    produtos = Produto.objects.all()
    pedidos = Pedido.objects.all()
    context = {
        'pedidos' : pedidos,
        'produtos': produtos,
    }
    return render(request, 'core/pedidos.html', context)

def login(request):
    return render(request, 'core/login.html')

def registro(request):
    # form = ClienteForm
    return render(request, 'core/registro.html')