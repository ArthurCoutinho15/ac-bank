from rest_framework import serializers
from accounts.models import Cliente, Agencia, Colaborador, Produto, Transacao, Conta

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class AgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agencia
        fields = '__all__'
        
class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'
        
class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = '__all__'

class ListaColaboradorAgenciaSerializer(serializers.ModelSerializer):
    colaborador_nome = serializers.ReadOnlyField(source='colaborador.nome')

    class Meta:
        model = Colaborador
        fields = ['colaborador_nome']