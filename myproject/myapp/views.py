# myapp/views.py
import requests
from django.http import HttpResponse
from .models import UserIP


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # Save the IP address to the database
    UserIP.objects.create(ip_address=ip)

    # Use ip-api.com to get the geolocation data of the IP address
    response = requests.get(f"http://ip-api.com/json/{ip}")
    geo_data = response.json()

    # Extract relevant fields (country, city, etc.)
    country = geo_data.get("country", "Unknown")
    city = geo_data.get("city", "Unknown")
    region = geo_data.get("regionName", "Unknown")

    return HttpResponse(f"Internal Server Error: CODE 500")