from django.contrib import admin

# Register your models here.
from cliente_service.models import Clientes, EnderecoClientes

admin.site.register(Clientes)
admin.site.register(EnderecoClientes)