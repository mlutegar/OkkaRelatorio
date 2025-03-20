from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from backend.serializers import UserSerializer, RelatorioSerializer

from backend.models import User, Relatorio


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    perminssion_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    perminssion_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)