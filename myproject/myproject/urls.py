# myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp import views  # Import your app's views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ensure there's a view for the root URL
]
