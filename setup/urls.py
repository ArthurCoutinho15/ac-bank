from django.contrib import admin
from django.urls import path, include
from accounts.views import ClienteViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet, basename='Clientes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
