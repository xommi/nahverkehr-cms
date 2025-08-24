from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from .views import home

def health(_request):
    return JsonResponse({"status": "ok"}, status=200)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("health", health, name="health"),
]
