from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from .views.TinyUrlViewSet import TinyUrlViewSet
from .views.OfflineUrlViewSet import OfflineUrlViewSet
from .views.RedirectUrlView import RedirectUrlView

router = DefaultRouter()

router.register('tiny_url', TinyUrlViewSet, basename='tiny_url')
router.register('offline_url', OfflineUrlViewSet, basename='offline_url')

urlpatterns = [
    url(r'^u', RedirectUrlView.as_view(), name="u"),
    url(r'shortener/', include(router.urls)),
]
