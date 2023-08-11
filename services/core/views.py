from rest_framework import mixins, viewsets

from core.models import UploadedImage
from core.serializers import UploadedImageSerializer


class UploadedImageViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.accounts.first())
