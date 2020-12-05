from django_multitenant.models import *


class UserTenant(TenantModel):
    tenant_id = 'id'
    token = models.TextField(default='')

    def __str__(self):
        return self.token


class Item(TenantModel):
    usertenant = models.ForeignKey(UserTenant, on_delete=models.CASCADE, default='', related_name="item")
    tenant_id = "usertenant_id"
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()
    is_available = models.BooleanField()
    picture = models.CharField(max_length=500000, default="")

    class Meta(object):
        unique_together = ["id", "usertenant"]