# Generated by Django 4.0.4 on 2022-05-18 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_estoqueentrada_estoquesaida'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estoquesaida',
            options={'verbose_name': 'estoque saída', 'verbose_name_plural': 'estoque saída'},
        ),
    ]