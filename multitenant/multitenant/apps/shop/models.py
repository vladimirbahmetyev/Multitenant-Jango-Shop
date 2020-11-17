from django.db import models


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()
    is_available = models.BooleanField()
    picture = models.FileField()
