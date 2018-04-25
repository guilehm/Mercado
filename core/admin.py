from django.contrib import admin
from .models import Cliente
from .models import Produto
from .models import Pedido
from .models import DetalhePedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'criado', 'modificado', ]

    list_filter = ['cliente', ]
    search_fields = ['cliente__cliente', 'id']

class DetalhePedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'produto', 'quantidade','preco', ]

    list_filter = ['pedido', 'produto','preco' ]
    search_fields = ['pedido', 'produto','preco']



admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(DetalhePedido, DetalhePedidoAdmin)
admin.site.register(Pedido, PedidoAdmin)