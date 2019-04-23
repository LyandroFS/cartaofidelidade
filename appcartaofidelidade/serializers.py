# coding=utf-8
from datetime import time, datetime

import pycep_correios
import json, requests
from django.contrib.auth.models import User, Group
from django.forms import DateField
from django.http import JsonResponse
from requests import Response
from rest_framework import serializers, status
from rest_framework.exceptions import APIException

from appcartaofidelidade.models import  Registros, Servicos, Premios


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')

#class EnderecoClientesSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = EnderecoClientes
#        fields = ('endereco', 'bairro','cidade','complemento','complemento2','uf',)
#
#class ClientesSerializer(serializers.ModelSerializer):
#    endereco = EnderecoClientesSerializer(read_only=True)
#    #endereco = serializers.StringRelatedField(many=False)
#
#
#    class Meta:
#        model = Clientes
#        fields = ('nome', 'email','cpf', 'cep','endereco')
#
#   def create(self, validated_data):
#        # message = validated_data.pop('message')
#        # message_obj = super().create(validated_data)
#        # send_mail(
#        #    'Invitation',
#        #    message,
#        #    'exampleemail@gmail.com',
#        #    [message_obj.recipient]
#        # )
#
#       endereco = pycep_correios.consultar_cep(validated_data['cep'])
#        cliente = Clientes.objects.create(**validated_data)
#
#
#
#       enderecoCliente = EnderecoClientes(cliente_id=cliente.cpf,
#                                           endereco=endereco['end'],
#                                           bairro=endereco['bairro'],
#                                           cidade=endereco['cidade'],
#                                           complemento=endereco.get('complemento', '-----'),
#                                           complemento2=endereco.get('complemento2', '-----'),
#                                           uf=endereco['uf'],
#                                           cep=endereco['cep'])
#
#        enderecoCliente.save()
#        return cliente




'''class EmpresasSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Empresas
        fields = ('idempresas','nome')
'''

class RegistrosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registros
        fields = ('id','data','servico','cliente','status')

    def create(self, validated_data):

        clienteCpf = validated_data['cliente']
        codServico = validated_data['servico']

        #Verifica se existe cliente ===================================================================================================
        url = 'http://127.0.0.1:8000/cliente_service/v1/clientes/?nome=&email=&cpf='+str(clienteCpf)
        headers = {'Authorization': 'Token f6e1ab7af9980147efde3876ad1984fb7c64782c'}
        response = requests.get(url, headers=headers)

        if response.status_code != 200 or response.json()['count'] == 0:
            raise APIException("Cliente não cadastrado. Para cadastrar um novo cliente acesse: http://127.0.0.1:8000/cliente_service/v1/clientes/?format=api")

        # Verifica se existe o serviço ===================================================================================================
        url = 'http://127.0.0.1:8000/servicos/?cod_servico=' + str(codServico)
        headers = {'Authorization': 'Token f6e1ab7af9980147efde3876ad1984fb7c64782c'}
        response = requests.get(url, headers=headers)

        data_servico = response.json()
        if response.status_code != 200 or data_servico['count'] == 0:
            raise APIException(
                "Serviço não cadastrado. Para cadastrar um novo serviço acesse: http://127.0.0.1:8000/servicos/?format=api")

        # Verifica se ja bateo o valor ===================================================================================================
        results = data_servico['results']
        #quantidade de entrada para contemplação
        qtdEntradas = results[0]['entradas']
        #validade da promoção
        validade = datetime.strptime(results[0]['validade'], '%Y-%m-%d').date()

        present = datetime.now().date()
        #present = datetime.strptime(validated_data['data'], '%Y-%m-%d')

        if(present > validade):
            raise APIException("Não é possível inserir o registro. A promoção expirou em: "+validade.strftime('%d/%m/%Y'))


        #url = 'http://127.0.0.1:8000/registros/?cliente=' + str(clienteCpf)+'&servico='+ str(codServico)
        url = 'http://127.0.0.1:8000/registros/?data=&status=true&cliente=' + str(clienteCpf) + '&servico=' + str(codServico)
        headers = {'Authorization': 'Token f6e1ab7af9980147efde3876ad1984fb7c64782c'}
        response = requests.get(url, headers=headers)

        if response.json()['count'] >= qtdEntradas:
            raise APIException(
                "Este cartão já alconçou o numero de entradas, seu prêmio já pode ser resgatado em: http://127.0.0.1:8000/premios/?format=api")

        #raise APIException(validated_data)
        registro = Registros.objects.create(**validated_data)
        return registro



class ServicosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Servicos
        fields = ('cod_servico','idempresa','descricao','validade','entradas', 'premio')

    def create(self, validated_data):

        idEmpresa = validated_data['idempresa']

        url = 'http://127.0.0.1:8000/empresas_service/v1/empresas/'+str(idEmpresa)+'/?format=json'
        headers = {'Authorization': 'Token f6e1ab7af9980147efde3876ad1984fb7c64782c'}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise APIException("Empresa não encontrada. Para cadastrar uma nova empressa acesse: http://127.0.0.1:8000/empresas_service/v1/empresas/?format=api")
            #reddit_data = response.json()

        servico = Servicos.objects.create(**validated_data)
        return servico



class PremiosSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Premios
        fields = ('data','servico','cliente','baixado')

    def resetarRegistros(self, clienteCpf,codServico):
        for obj in Registros.objects.filter(cliente=clienteCpf, status=True, servico=codServico):
            obj.status = False
            obj.save()
            #obj.__dict__

    def create(self, validated_data):

        clienteCpf = validated_data['cliente']
        codServico = validated_data['servico']

        # Verifica se existe cliente ===================================================================================================
        url = 'http://127.0.0.1:8000/cliente_service/v1/clientes/?nome=&email=&cpf=' + str(clienteCpf)
        headers = {'Authorization': 'Token f6e1ab7af9980147efde3876ad1984fb7c64782c'}
        response_clientes = requests.get(url, headers=headers)

        print(response_clientes.status_code)

        if response_clientes.status_code != 200 or response_clientes.json()['count'] == 0:
            raise APIException(
                "Cliente não cadastrado. Para cadastrar um novo cliente acesse: http://127.0.0.1:8000/cliente_service/v1/clientes/?format=api")

        # Verifica se existe o cliente encontra-se registrado no serviço ===================================================================================================
        url = 'http://127.0.0.1:8000/servicos/?cod_servico=' + str(codServico)
        headers = {'Authorization': 'Token f6e1ab7af9980147efde3876ad1984fb7c64782c'}
        response_servicos = requests.get(url, headers=headers)

        data_servico = response_servicos.json()
        if response_servicos.status_code != 200 or data_servico['count'] == 0:
            raise APIException(
                "Serviço não cadastrado. Para cadastrar um novo serviço acesse: http://127.0.0.1:8000/servicos/?format=api")

        results = data_servico['results']
        qtdEntradas = results[0]['entradas']

        # validade da promoção
        validade = datetime.strptime(results[0]['validade'], '%Y-%m-%d').date()

        present = datetime.now().date()
        # present = datetime.strptime(validated_data['data'], '%Y-%m-%d')

        if (present > validade):
            self.resetarRegistros(clienteCpf,codServico)
            raise APIException(
                "Não é possível resgatar o prêmio. A promoção expirou em: " + validade.strftime('%d/%m/%Y'))


        # Verifica se ja bateo o valor ===================================================================================================

        #url = 'http://127.0.0.1:8000/registros/?cliente=' + str(clienteCpf) + '&limit='+ str(qtdEntradas)+'&servico=' + str(codServico)
        url = 'http://127.0.0.1:8000/registros/?data=&status=true&cliente=' + str(clienteCpf) + '&limit='+ str(qtdEntradas)+ '&servico=' + str(codServico)
        headers = {'Authorization': 'Token f6e1ab7af9980147efde3876ad1984fb7c64782c'}
        response = requests.get(url, headers=headers)


        if response.json()['count'] < qtdEntradas:
            raise APIException(
                 "Este cartão ainda não atingiu a quantidade de registros necessários para resgatar o prêmio")


        #for result in response.json()['results']:
        #    print(result)
        #    obj = Registros.objects.get(pk=result['id'])
        #    obj.status = False
        #    obj.save()


        # quantidade de entrada para contemplação




        url = 'http://127.0.0.1:8000/premios/?cliente=' + str(clienteCpf) + '&servico=' + str(codServico)
        headers = {'Authorization': 'Token f6e1ab7af9980147efde3876ad1984fb7c64782c'}
        response = requests.get(url, headers=headers)

        # Verifica se ja bateo o valor ===================================================================================================
        data_servico = response.json()
        results = data_servico['results']

        if response.status_code != 200 or response.json()['count'] > 0 and validated_data['baixado'] == True:
            raise APIException(
                "Você já resgatou seu prêmio em: " + results[0]['data'])

        self.resetarRegistros(clienteCpf, codServico)

        validated_data['baixado'] = True

        premio = Premios.objects.create(**validated_data)
        return premio