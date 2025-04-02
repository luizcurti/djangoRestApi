from django.contrib import admin
from django.urls import path, include
from rest_framework import viewsets, routers
from core.views import ClienteViewSet


router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
