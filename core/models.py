from django.db import models

# Create your models here.
class Cliente(models.Model):
    cliente     = models.CharField('Nome Cliente', max_length=15)
    cpf         = models.CharField('CPF', max_length=11)

    def __str__(self):
        return self.cliente


class Produto(models.Model):
    produto     = models.CharField('Nome Produto', max_length=20)
    descricao   = models.TextField('Descrição', max_length=500)
    preco       = models.DecimalField('Preço', decimal_places=2, max_digits=7)

    def __str__(self):
        return self.produto


class Pedido(models.Model):
    cliente     = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    criado      = models.DateField('Criado em', auto_now_add=True)
    modificado  = models.DateField('Modificado em', auto_now_add=False, auto_now=True)

class DetalhePedido(models.Model):
    pedido      = models.ForeignKey(Pedido)
    produto     = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade  = models.PositiveSmallIntegerField('quantidade')
    preco       = models.DecimalField('Preço', decimal_places=2, max_digits=7)

    def __str__(self):
        return str(self.pedido)