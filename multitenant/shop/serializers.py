from rest_framework import serializers
from .models import Item, StoreAdmin


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class AdminSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = StoreAdmin
        fields = '__all__'