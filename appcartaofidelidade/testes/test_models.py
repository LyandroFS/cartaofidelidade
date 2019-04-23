# coding=utf-8

from django.test import TestCase
from model_mommy import mommy
from django.utils.timezone import datetime

from appcartaofidelidade.models import Clientes

class TestClientes(TestCase):

    def setUp(self):
        self.cliente = mommy.make(Clientes, nome='Vidal', email='vidal@gmail.com')

    def teste_cliente_creation(self):
        self.assertTrue(isinstance(self.cliente, Clientes))
        self.assertEqual(self.cliente.__str__(), self.cliente.nome)