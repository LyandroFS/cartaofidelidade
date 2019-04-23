# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from datetime import date

from django.db import models
from django.utils import timezone


'''class Clientes(models.Model):
    nome = models.CharField(max_length=80)
    cpf = models.CharField(blank=True,unique=True, primary_key=True, max_length=11)
    email = models.CharField(max_length=80, blank=True, null=True)
    cep = models.CharField(blank=False, max_length=13)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = "clientes"
        managed = True
        db_table = 'Clientes'

    def __str__(self):
        return self.nome
'''
'''class EnderecoClientes(models.Model):
    #cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    cliente = models.OneToOneField(Clientes, on_delete=models.CASCADE, related_name='endereco')
    endereco = models.CharField(blank=True, max_length=80, null=True)
    bairro = models.CharField(blank=True, max_length=50,null=True)
    cidade = models.CharField(blank=True, max_length=50, null=True)
    complemento = models.CharField(blank=True,  max_length=70, null=True)
    complemento2 = models.CharField(max_length=70, null=True)
    uf = models.CharField(blank=True, max_length=11, null=True)
    cep = models.CharField(blank=True, max_length=13, null=True)

    class Meta:
        verbose_name = 'Endereco Cliente'
        verbose_name_plural = "Endereco Clientes"
        managed = True
        db_table = 'EnderecoClientes'

    def __str__(self):
        return self.cep
'''

'''class Empresas(models.Model):
    idempresas = models.IntegerField(db_column='idEmpresas', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = "empresas"
        managed = True
        db_table = 'Empresas'

    def __str__(self):
        return self.nome
'''

class Servicos(models.Model):
    idempresa = models.IntegerField(db_column='idEmpresa', blank=True, null=True)  # Field name made lowercase.
    cod_servico = models.CharField(max_length=50 , unique=True, null=True)
    descricao = models.CharField(max_length=200)
    validade = models.DateField()
    entradas = models.IntegerField(default=10)  # This field type is a guess.
    #empresas_idempresas = models.IntegerField(db_column='Empresas_idEmpresas')  # Field name made lowercase.
    premio = models.TextField()

    class Meta:
        verbose_name = 'serviço'
        verbose_name_plural = "serviços"
        managed = True
        db_table = 'Servicos'

    def __str__(self):
        return self.descricao

class Registros(models.Model):
    #data = models.DateField(editable=False, default=timezone.now)
    id = models.AutoField(primary_key=True)
    data = models.DateField(default=date.today, editable=False)
    servico = models.IntegerField(blank=False, null=True)  # This field type is a guess.select * from Servicos
    cliente = models.IntegerField(blank=False)

    status = models.BooleanField(default=True, editable=False)
    #servicos_idempresa = models.IntegerField(db_column='Servicos_idEmpresa')  # Field name made lowercase.
    #servicos = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    #cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    #clientes_cpf = models.CharField(db_column='Clientes_cpf', max_length=11)  # Field name made lowercase.

    class Meta:
        verbose_name = 'registro'
        verbose_name_plural = "registros"
        managed = True
        db_table = 'Registros'

    def __str__(self):
        return self.data.strftime('%m/%d/%Y')


class Premios(models.Model):
    """docstring for Premios"""

    class Meta:
        verbose_name_plural = "premios"

    data = models.DateTimeField(default=timezone.now, editable=False)
    #servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    servico = models.IntegerField(blank=False)
    cliente = models.IntegerField(blank=False)
    #cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    baixado = models.BooleanField(default=False)

    def __str__(self):
        return self.data.strftime('%m/%d/%Y')


