from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('products/', views.ItemsList.as_view(), name='products'),
    path('products/create/', views.ItemCreate.as_view(), name="create-item"),
    path('products/update/<str:pk>/', views.ItemUpdate.as_view(), name="product-update"),
    path('products/delete/<str:pk>/', views.ItemDelete.as_view(), name="product-delete"),
    path('login/', obtain_auth_token),
]
