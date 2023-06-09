# Generated by Django 4.2 on 2023-04-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_medicamento_lote_alter_medicamento_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=50)),
                ('fecha_pedido', models.DateField()),
                ('productos', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
            ],
        ),
    ]
