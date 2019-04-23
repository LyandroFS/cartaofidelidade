from django.contrib import admin

# Register your models here.

from .models import Servicos, Registros, Premios

admin.site.register(Servicos)
admin.site.register(Registros)
admin.site.register(Premios)