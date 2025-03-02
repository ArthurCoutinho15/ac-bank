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

class AgenciaDetalhesSerializer(serializers.ModelSerializer):
    colaboradores = ColaboradorSerializer(many=True, read_only=True, source='colaborador_set')
    clientes = serializers.SerializerMethodField()

    class Meta:
        model = Agencia
        fields = ['id', 'nome', 'codigo', 'endereco', 'telefone', 'colaboradores', 'clientes']
    
    def get_clientes(self, obj):
        """Retorna a lista de clientes que possuem conta nesta agência"""
        contas = Conta.objects.filter(agencia=obj)  # Todas as contas da agência
        clientes = {conta.cliente for conta in contas}  # Pegamos apenas os clientes únicos
        return ClienteSerializer(clientes, many=True).data
    

class  ClienteContaSerializer(serializers.ModelSerializer):
    contas = ContaSerializer(many=True, read_only=True, source='conta_set')
    
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'telefone', 'endereco', 'data_cadastro', 'contas']

class ContaTransacoesSerializer(serializers.ModelSerializer):
    transacoes = TransacaoSerializer(many=True, read_only=True, source='transacao_set')
    
    class Meta:
        model = Conta
        fields = ['id', 'tipo', 'saldo', 'data_abertura', 'cliente', 'agencia', 'transacoes']