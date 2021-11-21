from django.db import models


class Venda(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return "{}. {}".format(str(self.id), self.title)