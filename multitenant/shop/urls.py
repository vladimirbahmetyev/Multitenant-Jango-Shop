from django.urls import path

from shop import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('products/', views.itemsList, name='products'),
    path('products/create/', views.itemCreate, name="create-item"),
    path('products/<str:pk>/', views.itemUpdate, name="product-update"),
    path('products/<str:pk>/', views.itemDelete, name="product-delete"),
    path('login/', obtain_auth_token),
]