from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from cliente_service.models import EnderecoClientes, Clientes
from cliente_service.serializers import EnderecoClientesSerializer, ClientesSerializer


class EnderecoClientesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = EnderecoClientes.objects.all()
    serializer_class = EnderecoClientesSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    __basic_fields =  ('nome', 'email','cpf')
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    #filter_backends = (filters.SearchFilter,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields
    #filter_class = ClienteFilter
    #together = ['nome']
    #search_fields = ('id','nome', 'email','cpf')
