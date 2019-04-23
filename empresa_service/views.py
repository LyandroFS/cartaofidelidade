from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from empresa_service.models import Empresas
from empresa_service.serializers import EmpresasSerializer


class EmpresasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer