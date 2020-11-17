from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item
from django_multitenant.utils import set_current_tenant
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings


# Create your views here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@api_view(['GET'])
def apiOverview(request):
    # return JsonResponse("API baser point", safe=False)
    api_urls = {
        'test': 'complete',
    }
    return Response(api_urls)


@api_view(['GET'])
def itemsList(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

# @permission_classes((IsAuthenticated,))
@api_view(['POST'])
def itemCreate(request):
    t = current_tenant
    set_current_tenant(t)
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def itemUpdate(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def itemDelete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()
    return Response("Item was successfully deleted")
