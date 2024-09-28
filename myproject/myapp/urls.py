# myapp/urls.py
from django.urls import path
from .views import get_client_ip

urlpatterns = [
    path('', get_client_ip, name='home'),  # Mapping the root path to get_client_ip
]