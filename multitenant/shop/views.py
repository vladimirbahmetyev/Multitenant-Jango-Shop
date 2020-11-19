from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ItemSerializer, UserTenantSerializer
from .models import Item, UserTenant
from django_multitenant.utils import set_current_tenant, unset_current_tenant
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def items_list(request):
    tenant_token = request.headers.get("Authorization").split(' ')[-1]
    tenant = UserTenant.objects.get(token=tenant_token)
    set_current_tenant(tenant)
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    unset_current_tenant()
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def item_create(request):
    tenant_token = request.headers.get("Authorization").split(' ')[-1]
    tenant = UserTenant.objects.get(token=tenant_token)
    set_current_tenant(tenant)
    data = request.data
    usertenant = UserTenantSerializer(tenant, data=data)
    if usertenant.is_valid():
        data["usertenant"] = usertenant.data
        data["usertenant_id"] = usertenant.data["id"]
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

        unset_current_tenant()
        return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def item_update(request, pk):
    tenant_token = request.headers.get("Authorization").split(' ')[-1]
    tenant = UserTenant.objects.get(token=tenant_token)
    set_current_tenant(tenant)
    item = Item.objects.get(id=pk)
    data = request.data
    usertenant = UserTenantSerializer(tenant, data=data)
    if usertenant.is_valid():
        data["usertenant"] = usertenant.data
        data["usertenant_id"] = usertenant.data["id"]
        serializer = ItemSerializer(instance=item, data=data)
        if serializer.is_valid():
            serializer.save()
        unset_current_tenant()
        return Response(serializer.data)


@csrf_exempt
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def item_delete(request, pk):
    tenant_token = request.headers.get("Authorization").split(' ')[-1]
    tenant = UserTenant.objects.get(token=tenant_token)
    set_current_tenant(tenant)
    item = Item.objects.get(id=pk)
    item.delete()
    unset_current_tenant()
    return Response({"result": True})
