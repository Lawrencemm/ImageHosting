import PIL.Image

from io import BytesIO

from celery import shared_task
from django.core.files import File

from core.models import UploadedImage, Thumbnail


@shared_task
def generate_thumbnails(image_id):
    uploaded_image = UploadedImage.objects.get(id=image_id)
    for thumb_type in uploaded_image.account.plan_type.thumbnail_types.all():
        image_file = uploaded_image.image.open()
        image = PIL.Image.open(image_file)
        image.thumbnail((thumb_type.height, thumb_type.height))
        image.save("test_thumbnail.jpg")
        Thumbnail.objects.create(
            uploaded_image=uploaded_image, image=File("test_thumbnail.jpg"), thumbnail_type=thumb_type)
