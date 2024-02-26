
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import SuppliersView
router = DefaultRouter()
router.register(r'', SuppliersView, basename='')


urlpatterns = [
    path('', include(router.urls)),
]
