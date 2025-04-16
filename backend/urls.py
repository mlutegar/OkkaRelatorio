from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views
from .views import UserViewSet, RelatorioViewSet, CadastroView, RelatorioPorUsuarioView, RelatorioPorSetorView
from django.urls import path

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'relatorios', RelatorioViewSet)

urlpatterns = [
                  path('login/', obtain_auth_token, name='api_token_auth'),
                  path('cadastro/', CadastroView.as_view(), name='cadastro'),
                  path('relatorios/setor/<str:setor>/', RelatorioPorSetorView.as_view(), name='relatorios-por-setor'),
                  path('relatorios/<str:username>/', RelatorioPorUsuarioView.as_view(), name='relatorios-por-usuario'),
                  path('export-excel/', views.export_excel, name='export_excel'),
              ] + router.urls
