from django.db.models import signals
from django.dispatch import receiver

from core.models import UploadedImage
from image_processing.process_image import generate_thumbnails


@receiver(signals.post_save, sender=UploadedImage)
def on_image_saved(sender, instance, created, update_fields, *args, **kwargs):
    if created or "image" in update_fields:
        generate_thumbnails(instance.id)
