from django.urls import path, include
from rest_framework import routers

from live import views

router = routers.DefaultRouter()
router.register('programs', views.ProgramViewSet)

urlpatterns = [
    path('', include(router.urls))
]
