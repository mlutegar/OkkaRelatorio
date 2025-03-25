from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RelatorioViewSet, CadastroView
from django.urls import path

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'relatorios', RelatorioViewSet)

urlpatterns = [
                  path('login/', obtain_auth_token, name='api_token_auth'),
                  path('cadastro/', CadastroView.as_view(), name='cadastro'),
              ] + router.urls
