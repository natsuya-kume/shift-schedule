from django.urls import path, include
from .views import StaffCreate

urlpatterns = [
    path('create/', StaffCreate.as_view(), name = "staffcreate"),
]