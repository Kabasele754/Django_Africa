
from django.urls import path

from app_inscription.views import home_index, list_view

urlpatterns = [
    path('',home_index, name="base"),
    path('list',list_view, name="list")
]