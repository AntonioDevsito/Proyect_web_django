from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("products_index",views.products, name="products" ),
]