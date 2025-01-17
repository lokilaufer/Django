from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []
