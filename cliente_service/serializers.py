# coding=utf-8
import pycep_correios
from rest_framework import serializers

from cliente_service.models import EnderecoClientes, Clientes


class EnderecoClientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EnderecoClientes
        fields = ('endereco', 'bairro','cidade','complemento','complemento2','uf',)

class ClientesSerializer(serializers.ModelSerializer):
    endereco = EnderecoClientesSerializer(read_only=True)
    #endereco = serializers.StringRelatedField(many=False)


    class Meta:
        model = Clientes
        fields = ('nome', 'email','cpf', 'cep','endereco')

    def create(self, validated_data):
        # message = validated_data.pop('message')
        # message_obj = super().create(validated_data)
        # send_mail(
        #    'Invitation',
        #    message,
        #    'exampleemail@gmail.com',
        #    [message_obj.recipient]
        # )

        endereco = pycep_correios.consultar_cep(validated_data['cep'])
        cliente = Clientes.objects.create(**validated_data)



        enderecoCliente = EnderecoClientes(cliente_id=cliente.cpf,
                                           endereco=endereco['end'],
                                           bairro=endereco['bairro'],
                                           cidade=endereco['cidade'],
                                           complemento=endereco.get('complemento', '-----'),
                                           complemento2=endereco.get('complemento2', '-----'),
                                           uf=endereco['uf'],
                                           cep=endereco['cep'])

        enderecoCliente.save()
        return cliente