# Generated by Django 3.2.9 on 2021-12-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20211207_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='product',
        ),
        migrations.AddField(
            model_name='venda',
            name='product',
            field=models.ManyToManyField(to='vendas.Produto'),
        ),
    ]
