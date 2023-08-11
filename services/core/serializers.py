from rest_framework import serializers

from core.models import UploadedImage, Account


class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage

    image = serializers.ImageField()
    account = serializers.RelatedField(queryset=Account.objects.all())
