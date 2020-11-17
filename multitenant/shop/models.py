# from django.db import models
from django.contrib.auth.models import User
from django_multitenant.fields import *
from django_multitenant.models import *


class Store(TenantModel):
    tenant_id = 'id'
    name = models.CharField(max_length=50)


class StoreAdmin(TenantModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    storeId = models.CharField(max_length=15)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default='')


class Item(TenantModel):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default='')
    tenant_id = "store_id"
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()
    is_available = models.BooleanField()

    class Meta(object):
        unique_together = ["id", "store"]

    def __str__(self):
        return self.item_name
