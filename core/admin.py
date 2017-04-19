from django.contrib import admin
from .models import *

class ContatoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'telefone')

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('Nome', 'CPF', 'Estado')

class FornecedorAdmin(admin.ModelAdmin):
	list_display = ('Nome', 'CNPJ', 'Estado')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('CPF', 'Nome', 'Email')

class VendaAdmin(admin.ModelAdmin):
    list_display = ('DataVenda', 'ValorTotal', 'Cliente')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('DataPedido', 'DataRecebimento', 'PrecoTotal', 'CodigoFornecedor')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('NomeProduto', 'Quantidade', 'MinQuantidade')

class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ('CodigoPedido', 'CodigoProduto', 'PrecoUnitario', 'Quantidade')

class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ('CodigoVenda', 'CodigoProduto', 'PrecoUnitario', 'Quantidade')

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)
admin.site.register(ItemVenda, ItemVendaAdmin)