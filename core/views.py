from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import resolve_url
from django.forms.models import inlineformset_factory
from .models import Produto
from .models import Pedido
from .models import DetalhePedido
from .forms import PedidoForm
from .forms import DetalhePedidoForm


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def produtos(request):
    produtos = Produto.objects.all()
    context = {
        'produtos':produtos,
    }
    return render(request, 'core/produtos.html', context)


def venda(request, venda_pk):
    pedido = Pedido.objects.get(pk=venda_pk)
    itens = pedido.detalhepedido_set.values()
    print('AQUI PRINTA ITENS\n', itens)
    context = {
        'pedido':pedido,
        'itens':itens,
    }
    return render(request, 'core/venda.html', context)


def pedidos(request):
    produtos = Produto.objects.all()
    pedidos = Pedido.objects.all()

    pedido_forms = Pedido()
    item_pedido_formset = inlineformset_factory(
        Pedido, DetalhePedido, form=DetalhePedidoForm,extra=0, can_delete=False, min_num=1, validate_min=True
    )

    if request.method == 'POST':
        forms = PedidoForm(request.POST, request.FILES,
                           instance=pedido_forms, prefix='main')
        formset = item_pedido_formset(
            request.POST, request.FILES, instance=pedido_forms, prefix='produto'
        )

        if forms.is_valid() and formset.is_valid():
            forms = forms.save()
            formset.save()
            return HttpResponseRedirect(resolve_url('core:pedidos', forms.pk))

    else:
        forms = PedidoForm(instance=pedido_forms, prefix='main')
        formset = item_pedido_formset(instance=pedido_forms, prefix='produto')

    context = {
        'pedidos' : pedidos,
        'produtos': produtos,
        'forms' : forms,
        'formset' : formset,
    }
    return render(request, 'core/pedidos.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            return redirect('core:index')
        else:
            return render(request, 'core/login.html', {'login_form':form})
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'login_form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:index'))


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            form.save()
            return redirect('core:index')
        else:
            if form.errors:
                return render(request,'core/registro.html', context)
    else:
        form = UserCreationForm()
        context = {'form':form}
        return render(request, 'core/registro.html', context)