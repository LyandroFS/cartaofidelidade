# coding=utf-8
from rest_framework import serializers
from empresa_service.models import Empresas

class EmpresasSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Empresas
        fields = ('idempresas','nome')