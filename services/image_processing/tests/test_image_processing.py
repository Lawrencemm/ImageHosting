import os

import pytest
from django.contrib.auth.models import User
from django.core.files import File

from core.models import UploadedImage, Account, PlanType, ThumbnailType, Thumbnail


@pytest.mark.django_db
def test_image_processing():
    user = User.objects.create()
    plan_type = PlanType.objects.create()
    thumb_type = ThumbnailType.objects.create(height=50)
    plan_type.thumbnail_types.add(thumb_type)
    account = Account.objects.create(plan_type=plan_type)
    account.users.add(user)

    image = UploadedImage(account=account)
    image.image.name = os.path.dirname(os.path.abspath(__file__)) + "/cat.jpg"
    image.save()

    assert Thumbnail.objects.filter(uploaded_image=image, thumbnail_type=thumb_type).exists()
