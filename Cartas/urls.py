from rest_framework import routers
from .api import CartasViewSet

router = routers.DefaultRouter()

router.register('api/cards', CartasViewSet, 'Cartas')

urlpatterns = router.urls
