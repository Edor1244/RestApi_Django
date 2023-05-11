from rest_framework import routers
from .api import CartasViewSet

router = routers.DefaultRouter()

router.register('api/Cartas', CartasViewSet, 'Cartas')

urlpatterns = router.urls
