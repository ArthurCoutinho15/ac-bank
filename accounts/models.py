from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    telefone = models.CharField(max_length=14, blank=False, null=False)
    endereco = models.CharField(max_length=150, blank=False, null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

class Agencia(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    codigo = models.CharField(max_length=10, unique=True)
    endereco = models.CharField(max_length=50, blank=False, null=False)
    telefone = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome
    

class Colaborador(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    telefone = models.CharField(max_length=14, blank=False, null=False)
    endereco = models.CharField(max_length=150, blank=False, null=False)
    data_admissao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nome

class Conta(models.Model):
    TIPO_CONTA_CHOICES = [
        ('CC', 'Conta corrente'),
        ('CP', 'Conta poupança'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    agencia = models.ForeignKey(Agencia, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=2, choices=TIPO_CONTA_CHOICES)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_abertura = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.cliente} | {self.agencia} | {self.tipo}'


class Produto(models.Model):
    TIPO_PRODUTO_CHOICES = [
        ('EMP', 'Empréstimos'),
        ('CAR', 'Cartão de Crédito'),
        ('SEG', 'Seguros'),
        ('SER', 'Serviços'),
        ('SAU', 'Plano de Saúde'),
    ]
    
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=3, choices=TIPO_PRODUTO_CHOICES)
    descricao = models.TextField()
    taxa_juros = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    limite_credito = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Transacao(models.Model):
    TIPO_TRANSACAO_CHOICES = [
        ('DEP', 'Depósito'),
        ('SAQ', 'Saque'),
        ('PIX', 'Pix'),
        ('PAG', 'Pagamento')
    ]
    
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=3, choices=TIPO_TRANSACAO_CHOICES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return f'{self.get_tipo_display()} - {self.valor}'