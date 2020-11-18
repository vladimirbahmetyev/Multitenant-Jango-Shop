from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item, UserTenant
from django_multitenant.utils import set_current_tenant, unset_current_tenant
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.http import JsonResponse
from django.db.models.signals import post_save
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return None


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Test Api
# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'test': 'complete',
#     }
#     return Response(api_urls)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((CsrfExemptSessionAuthentication,))
def itemsList(request):
    tenant_token = request.headers.get("Authorization").split(' ')[-1]

    tenant = UserTenant.objects.get(token=tenant_token)
    set_current_tenant(tenant)
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    unset_current_tenant()
    response = JsonResponse({"data": serializer.data})

    response['Access-Control-Allow-Origin'] = '*'
    response["Access-Control-Allow-Headers"] = '*'
    return response


# @permission_classes((IsAuthenticated,))
@api_view(['POST'])
def itemCreate(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# @permission_classes((IsAuthenticated,))
@api_view(['POST'])
def itemUpdate(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# @permission_classes((IsAuthenticated,))
@api_view(['POST'])
def itemDelete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response("Item was successfully deleted")
