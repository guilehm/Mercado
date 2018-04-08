from django.contrib import admin
from .models import Cliente
from .models import Produto
from .models import Pedido

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido)