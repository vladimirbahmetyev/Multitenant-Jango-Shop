# from django.db import models
from django_multitenant.fields import *
from django_multitenant.models import *


class UserTenant(TenantModel):
    tenant_id = 'id'
    token = models.TextField(default='')

    def __str__(self):
        return self.token


class Item(TenantModel):
    user = models.ForeignKey(UserTenant, on_delete=models.CASCADE, default='')
    tenant_id = "id"
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()
    is_available = models.BooleanField()
#
#     def __str__(self):
#         return self.item_name
