from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('tags', TagViewSet, basename='tag')
router.register('userprofiles', UserProfileViewSet, basename='userprofile')

urlpatterns = [
    path('', include(router.urls)),
]
