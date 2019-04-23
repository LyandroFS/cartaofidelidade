from django.db import models

# Create your models here.

class Clientes(models.Model):
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

class EnderecoClientes(models.Model):
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
        verbose_name = 'Endereço Cliente'
        verbose_name_plural = "Endereço Clientes"
        managed = True
        db_table = 'EnderecoClientes'

    def __str__(self):
        return self.cep