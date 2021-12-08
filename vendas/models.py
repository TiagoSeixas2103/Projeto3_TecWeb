from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    cost = models.FloatField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return "{}".format(self.name)

class Venda(models.Model):
    title = models.CharField(max_length=200)
    quantity = models.IntegerField()
    product = models.ManyToManyField(Produto)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return "{}".format(self.title)

