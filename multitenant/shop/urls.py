from django.urls import path

from shop import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('products/', views.items_list, name='products'),
    path('products/create/', views.item_create, name="create-item"),
    path('products/<str:pk>/', views.item_update, name="product-update"),
    path('products/delete/<str:pk>/', views.item_delete, name="product-delete"),
    path('login/', obtain_auth_token),
]
