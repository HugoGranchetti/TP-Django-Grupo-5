from django.contrib import admin

from django.contrib import admin
from .models import Medicamento, Proveedor,Pedido,Cliente,stock_User

# Registro de modelos en el panel de administración
admin.site.register(Medicamento)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(stock_User)

