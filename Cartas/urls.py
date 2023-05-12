from rest_framework import routers
from .api import CartasViewSet, UserViewSet, UserCardsViewSet

router = routers.DefaultRouter()

router.register('api/cards', CartasViewSet, 'cards')
router.register('api/users', UserViewSet, 'users')
router.register('api/usercards', UserCardsViewSet, 'usercards')

urlpatterns = router.urls
