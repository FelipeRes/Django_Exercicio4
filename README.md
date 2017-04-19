# Django_Exercicio4


## Questão 2)
python manage.py shell

import django

django.setup()

from core.models import Cliente

cliente = Cliente(CPF="06072365311",Nome="Rogerio",Cidade="Teresina",Endereco="Rua Piaui",CEP="64008011",FoneResidencial="8873212123",RendaFamiliar=200,Email="rogerio@gmail.com")

cliente.save()

from core.models import Produto

produto = Produto(NomeProduto="Sabonete",Quantidade=10,MinQuantidade=20)

produto.save()

from core.models import Fornecedor

fornecedor = Fornecedor(CNPJ="010349581030413",Nome="Super Fornecedor", Endereco="Rua Elisandro", Cidade="Luis Correia", Estado="Piaui", CEP="65003010",Fone= "32157219")

fornecedor.save()

from core.models import Pedido

pedido = Pedido(DataPedido=django.utils.timezone.now(),DataRecebimento=django.utils.timezone.now(),PrecoTotal=20,CodigoFornecedor=fornecedor)

pedido.save()

from core.models import Venda

venda = Venda(DataVenda=django.utils.timezone.now(),ValorTotal=10,Cliente=cliente)

venda.save()

from core.models import ItemVenda

itemVenda = ItemVenda(CodigoVenda=venda,CodigoProduto=produto,PrecoUnitario=10,Quantidade=10)

itemVenda.save()

from core.models import ItemPedido

itemPedido = ItemPedido(CodigoPedido=pedido,CodigoProduto=produto,PrecoUnitario=10,Quantidade=10)

itemPedido.save()

## Questão 3)

Cliente.objects.all()

Venda.objects.get(Cliente=Cliente.objects.get(pk=1))

Pedido.objects.get(pk=1)

ItemPedido.objects.get(CodigoPedido=Pedido.objects.get(id=1))

from django.db.models import F

 Produto.objects.get(Quantidade__gte=F("Quantidade"))


