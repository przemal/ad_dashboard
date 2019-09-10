from rest_framework import viewsets

from ad_statistics.models import Campaign
from ad_statistics.models import Source
from ad_statistics.models import Statistic
from ad_statistics.serializers import CampaignSerializer
from ad_statistics.serializers import SourceSerializer
from ad_statistics.serializers import StatisticSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all()


class SourceViewSet(viewsets.ModelViewSet):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()


class StatisticViewSet(viewsets.ModelViewSet):
    serializer_class = StatisticSerializer
    queryset = Statistic.objects.all()
