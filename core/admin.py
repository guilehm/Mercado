from django.contrib import admin
from .models import Cliente
from .models import Produto
from .models import Pedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'criado', 'modificado', ]

    list_filter = ['cliente', ]
    search_fields = ['cliente__cliente', 'id']

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido, PedidoAdmin)