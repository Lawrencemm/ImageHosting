from rest_framework import routers

from core.views import UploadedImageViewSet

router = routers.DefaultRouter()
router.register(prefix="image", viewset=UploadedImageViewSet, basename="images")

urlpatterns = []
urlpatterns += router.urls
