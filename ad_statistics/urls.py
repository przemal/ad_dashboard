from django.urls import include
from django.urls import path
from rest_framework import routers

from ad_statistics.views import CampaignViewSet
from ad_statistics.views import SourceViewSet
from ad_statistics.views import StatisticViewSet


router = routers.DefaultRouter()
router.register('campaigns', CampaignViewSet)
router.register('sources', SourceViewSet)
router.register('statistics', StatisticViewSet)


urlpatterns = [
    path('', include(router.urls))
]
