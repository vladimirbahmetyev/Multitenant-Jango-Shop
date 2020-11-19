from rest_framework import serializers
from .models import Item, UserTenant


class UserTenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTenant
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    usertenant_id = serializers.IntegerField()
    usertenant = UserTenantSerializer(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'
