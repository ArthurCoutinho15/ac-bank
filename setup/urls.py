from django.contrib import admin
from django.urls import path, include
from accounts.views import ClienteViewSet, ColaboradorViewSet, AgenciaViewSet, TransacaoViewSet, ProdutoViewSet, ContaViewSet, ListaColaboradorAgencia,\
AgenciaDetalhesView, ClienteContaViewSet, ContaTransacoesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet, basename='Clientes')
router.register('colaboradores', ColaboradorViewSet, basename='Colaboradores')
router.register('agencias', AgenciaViewSet, basename='Agencias')
router.register('transacoes', TransacaoViewSet, basename='Transacoes')
router.register('produtos', ProdutoViewSet, basename='Produtos')
router.register('contas', ContaViewSet, basename='Contas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('colaboradores/<int:pk>/agencias', ListaColaboradorAgencia.as_view()),
    path('agencias/<int:pk>/detalhes', AgenciaDetalhesView.as_view() ),
    path('clientes/<int:pk>/contas', ClienteContaViewSet.as_view() ),
    path('contas/<int:pk>/transacoes', ContaTransacoesViewSet.as_view()),
]
