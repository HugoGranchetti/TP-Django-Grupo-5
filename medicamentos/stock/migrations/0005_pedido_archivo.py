# Generated by Django 4.2 on 2023-04-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_pedido'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
