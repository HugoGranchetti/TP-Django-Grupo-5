# Generated by Django 4.2 on 2023-05-19 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_pedido_vendedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='direccion',
        ),
        migrations.AddField(
            model_name='cliente',
            name='cuit',
            field=models.CharField(max_length=100, null=True, verbose_name='CUIT'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='mail',
            field=models.EmailField(max_length=100, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='mail',
            field=models.EmailField(max_length=100, null=True, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='pais',
            field=models.CharField(max_length=200, null=True, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=20, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(max_length=20, null=True, verbose_name='Teléfono'),
        ),
    ]
