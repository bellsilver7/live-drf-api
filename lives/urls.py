from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from config import settings
from lives.views import ProgramViewSet

router = routers.DefaultRouter()
router.register('programs', ProgramViewSet)

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
