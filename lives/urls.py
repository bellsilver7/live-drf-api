from django.urls import path, include
from rest_framework import routers

from lives.views import ProgramViewSet

router = routers.DefaultRouter()
router.register('programs', ProgramViewSet)

urlpatterns = [
    path('', include(router.urls))
]
