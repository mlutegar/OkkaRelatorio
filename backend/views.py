from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from backend.serializers import UserSerializer, RelatorioSerializer, CadastroSerializer

from backend.models import User, Relatorio


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    lookup_field = 'username'

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class CadastroView(generics.CreateAPIView):
    serializer_class = CadastroSerializer
    permission_classes = [AllowAny]  # Permite que qualquer pessoa se cadastre


class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    perminssion_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)