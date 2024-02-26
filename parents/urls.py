
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ParentsView
router = DefaultRouter()
router.register(r'', ParentsView, basename='')


urlpatterns = [
    path('', include(router.urls)),
]
