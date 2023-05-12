from rest_framework import routers
from .api import CartasViewSet, UserViewSet, UserCardsViewSet

router = routers.DefaultRouter()

router.register('api/Cartas', CartasViewSet, 'Cartas')
router.register('api/User', UserViewSet, 'User')
router.register('api/UserCards', UserCardsViewSet, 'UserCards')


urlpatterns = router.urls
