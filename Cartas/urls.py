from django.urls import path, include
from rest_framework import routers
from .api import CartasViewSet, UserViewSet, UserCardsViewSet

router = routers.DefaultRouter()
router.register(r'api/cards', CartasViewSet)
router.register(r'api/users', UserViewSet)
router.register(r'api/usercards', UserCardsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
