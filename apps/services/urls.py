from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("services_index",views.services, name="services" ),  
]