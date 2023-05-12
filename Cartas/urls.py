from rest_framework import routers
from .api import CartasViewSet
from .api import UserViewSet
from .api import UserCardsViewSet

router = routers.DefaultRouter()

router.register('api/Cartas', CartasViewSet, 'Cartas')
router.register('api/User', UserViewSet, 'User')
router.register('api/UserCards', UserCardsViewSet, 'UserCards')


urlpatterns = router.urls
