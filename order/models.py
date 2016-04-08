from __future__ import unicode_literals

from django.db import models
from beer.models import Beer
from drinker.models import Drinker

class Order(models.Model):
    drinker = models.ForeignKey(Drinker, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    destination = models.TextField()
    # 1: new; 2: payed; 3: ready; 4:send to destination; 5:delivered
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)
    qty = models.SmallIntegerField()

    def __str__(self):
        return self.name
