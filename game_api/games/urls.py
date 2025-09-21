from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeveloperViewSet, PlatformViewSet, GameViewSet, UserViewSet


router = DefaultRouter()
router.register(r'developers', DeveloperViewSet)
router.register(r'platforms', PlatformViewSet)
router.register(r'games', GameViewSet)
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
]