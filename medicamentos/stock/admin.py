from django.contrib import admin
from .models import Cliente, Proveedor, Medicamento, Pedido

# Registro de modelos en el panel de administración
admin.site.register(Cliente)
admin.site.register(Proveedor)
admin.site.register(Medicamento)
admin.site.register(Pedido)