from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Produto
from .models import Pedido


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
                print('deu erro')
                print(dir(form.errors))
            return render(request,'core/registro.html', context)
    else:
        form = UserCreationForm()
        context = {'form':form}
        return render(request, 'core/registro.html', context)