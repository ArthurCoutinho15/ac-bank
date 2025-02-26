from rest_framework import viewsets
from accounts.serializers import ClienteSerializer, AgenciaSerializer, ColaboradorSerializer, ProdutoSerializer, TransacaoSerializer, ContaSerializer
from accounts.models import Cliente, Agencia, Colaborador, Produto, Transacao, Conta

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer