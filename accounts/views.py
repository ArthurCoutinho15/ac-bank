from rest_framework import viewsets, generics, filters
from accounts.serializers import ClienteSerializer, AgenciaSerializer, ColaboradorSerializer, ProdutoSerializer, TransacaoSerializer, ContaSerializer, ListaColaboradorAgenciaSerializer
from accounts.models import Cliente, Agencia, Colaborador, Produto, Transacao, Conta

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer
    
class AgenciaViewSet(viewsets.ModelViewSet):
    queryset = Agencia.objects.all().order_by('id')
    serializer_class = AgenciaSerializer
    
class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all().order_by('id')
    serializer_class = ColaboradorSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer

class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all().order_by('id')
    serializer_class = TransacaoSerializer
    
class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all().order_by('id')
    serializer_class = ContaSerializer

class ListaColaboradorAgencia(generics.RetrieveAPIView):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer

    def get_object(self):
        # Buscar o colaborador pelo ID
        colaborador = Colaborador.objects.get(id=self.kwargs['pk'])
        # Retornar a agência associada ao colaborador
        return colaborador.agencia