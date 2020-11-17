from django_multitenant.utils import set_current_tenant
from .models import StoreAdmin
from .serializers import AdminSerialaizer

class MultitenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.data)
        # if request.user and not request.user.is_anonymous:
        #     set_current_tenant(request.user.StoreAdmin.storeId)
        return self.get_response(request)