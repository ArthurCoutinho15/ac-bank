from rest_framework import serializers
from accounts.models import Cliente, Agencia, Colaborador, Produto, Transacao, Conta

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class AgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencia
        field = '__all__'
        
class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        field = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        field = '__all__'

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        field = '__all__'
        
class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        field = '__all__'
