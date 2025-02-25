from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False, null=False, unique=True)
    telefone = models.CharField(max_length=14, blank=False, null=False)
    endereco = models.CharField(max_length=150, blank=False, null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)

class Agencia(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    codigo = models.CharField(max_length=10, unique=True)
    endereco = models.CharField(max_length=50, blank=False, null=False)
    telefone = models.CharField(max_length=14)

class Conta(models.Model):
    TIPO_CONTA = [
        ('CC', 'Conta corrente'),
        ('CP', 'Conta poupança')
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    