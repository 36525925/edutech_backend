
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NotificationsView
router = DefaultRouter()
router.register(r'', NotificationsView, basename='')


urlpatterns = [
    path('', include(router.urls)),
]
