from django.contrib import admin
from django.urls import path
from .views import singin

urlpatterns = [
    path("singin/", singin, name="signin"),
]
