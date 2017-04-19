from django.db import models

# Create your models here.

class Contato(models.Model):
	nome = models.CharField(max_length=50)
	endereco = models.CharField(max_length=200)
	email = models.CharField(max_length=100)
	data_nascimento = models.DateField()
	telefone = models.CharField(max_length=20)

class Cliente(models.Model):
	CPF = models.CharField(max_length=14)
	Nome = models.CharField(max_length=30)
	Endereco = models.CharField(max_length=35)
	Complemento = models.CharField(max_length=50)
	Cidade = models.CharField(max_length=25)
	Estado = models.CharField(max_length=2)
	CEP = models.CharField(max_length=8)
	FoneResidencial = models.CharField(max_length=15)
	FoneTrabalho = models.CharField(max_length=15)
	RendaFamiliar = models.DecimalField(max_digits = 10 , decimal_places = 2)
	Email = models.EmailField()

	def __str__(self):
		return self.Nome

class Venda(models.Model):
    DataVenda = models.DateTimeField()
    ValorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.Cliente.Nome) + " - " + str(self.DataVenda) + " - " + str(self.ValorTotal) )


class Fornecedor(models.Model):
	CNPJ = models.CharField(max_length=20)
	Nome = models.CharField(max_length=30)
	Endereco = models.CharField(max_length=35)
	Complemento = models.CharField(max_length=50)
	Cidade = models.CharField(max_length=25)
	Estado = models.CharField(max_length=2)
	CEP = models.CharField(max_length=8)
	Fone = models.CharField(max_length=15)
	Responsavel = models.CharField(max_length=30)
	Wrbsite = models.CharField(max_length=80)

	def __str__(self):
		return self.Nome

class Produto(models.Model):
	NomeProduto = models.CharField(max_length=35)
	Quantidade = models.IntegerField()
	MinQuantidade = models.IntegerField()

	def __str__(self):
		return self.NomeProduto

class ItemVenda(models.Model):
    CodigoVenda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    CodigoProduto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    PrecoUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    Quantidade = models.IntegerField()

    def __str__(self):
    	return str(self.CodigoVenda) + ' - ' + str(self.CodigoProduto) + ' - ' + str(self.PrecoUnitario) + ' - ' + str(self.Quantidade)

class Pedido(models.Model):
    DataPedido = models.DateField()
    DataRecebimento = models.DateField()
    PrecoTotal = models.DecimalField(max_digits=10, decimal_places=2)
    CodigoFornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    def __str__(self):
    	return str(self.DataPedido) + ' - ' + str(self.DataRecebimento) + ' - ' + str(self.PrecoTotal) + ' - ' + str(self.CodigoFornecedor)

class ItemPedido(models.Model):
    CodigoPedido = models.ForeignKey(Pedido)
    CodigoProduto = models.ForeignKey(Produto)
    PrecoUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    Quantidade = models.IntegerField()

    def __str__(self):
    	return str(self.CodigoPedido) + ' - ' + str(self.CodigoProduto) + ' - ' + str(self.PrecoUnitario) + ' - ' + str(self.Quantidade)

