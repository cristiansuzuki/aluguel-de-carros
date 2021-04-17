from django.contrib import admin
from .models import *

class CarrosAdmin(admin.ModelAdmin):
    list_display = ['carro']
    list_filter = ['carro']
    search_fields = ['carro']

# Register your models here.
admin.site.register(Carros, CarrosAdmin)
admin.site.register(Clientes)
admin.site.register(Aluguel)