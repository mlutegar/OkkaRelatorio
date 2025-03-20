from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RelatorioViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'relatorios', RelatorioViewSet)

urlpatterns = router.urls
