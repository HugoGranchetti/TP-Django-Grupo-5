from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre", null=True)
    mail = models.EmailField(max_length=100, verbose_name="E-mail", null=True)
    telefono = models.CharField(max_length=20, verbose_name="Teléfono", null=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return f"{self.nombre} ({self.mail})"

class Cliente(Empresa):
    cuit = models.CharField(max_length=100, verbose_name="CUIT", null=True)

class Proveedor(Empresa):
    pais = models.CharField(max_length=200, verbose_name="País", null=True)

class Medicamento(models.Model):
    nombre = models.CharField(max_length=200)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_vencimiento = models.DateField()
    precio=models.IntegerField(default=0)
    lote=models.IntegerField(default=1)
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    nombre_cliente = models.CharField(max_length=50)
    fecha_pedido = models.DateField()
    productos = models.ManyToManyField(Medicamento)
    cantidad = models.IntegerField()
    proveedor=models.ManyToManyField(Proveedor)
    archivo = models.FileField(upload_to='uploads/', blank=True, null=True)

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)