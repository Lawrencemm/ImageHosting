from django.contrib.auth import get_user_model
from django.db import models


class ThumbnailType(models.Model):
    height = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.height}px"


class PlanType(models.Model):
    name = models.CharField(max_length=256)
    thumbnail_types = models.ManyToManyField(ThumbnailType, blank=True)
    has_original_link = models.BooleanField(default=False)
    has_expirable_links = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Account(models.Model):
    users = models.ManyToManyField(get_user_model(), related_name="accounts")
    plan_type = models.ForeignKey(PlanType, null=True, blank=True, on_delete=models.SET_NULL)


class UploadedImage(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    image = models.ImageField()


class Thumbnail(models.Model):
    uploaded_image = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    thumbnail_type = models.ForeignKey(ThumbnailType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="thumbnails")
