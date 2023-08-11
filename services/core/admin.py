from django.contrib import admin

from core.models import UploadedImage, PlanType, Account, ThumbnailType

admin.site.register(UploadedImage)
admin.site.register(PlanType)
admin.site.register(Account)
admin.site.register(ThumbnailType)
