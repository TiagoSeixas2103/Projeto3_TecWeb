# Generated by Django 3.2.9 on 2021-11-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_venda_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='cost',
            field=models.FloatField(default=5.5),
            preserve_default=False,
        ),
    ]
