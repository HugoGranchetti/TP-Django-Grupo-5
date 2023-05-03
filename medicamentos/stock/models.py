from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Medicamento(models.Model):
    id = models.IntegerField(primary_key=True)
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
    productos = models.ForeignKey(Medicamento,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    archivo = models.FileField(upload_to='uploads/', blank=True, null=True)
    vendedor=models.IntegerField(default=0)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class stock_User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
