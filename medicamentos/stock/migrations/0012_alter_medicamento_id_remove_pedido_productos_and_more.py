# Generated by Django 4.2 on 2023-05-21 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_remove_cliente_direccion_remove_proveedor_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(to='stock.medicamento'),
        ),
    ]
