# Generated by Django 4.2 on 2023-04-21 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_rename_user_stock_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='vendedor',
            field=models.IntegerField(default=0),
        ),
    ]
