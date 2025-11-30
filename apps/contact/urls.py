from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("contact_index",views.contact, name="contact" ),  
]