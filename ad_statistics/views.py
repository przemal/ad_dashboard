from typing import List

from django.db.models import Sum
from django.db.models import Value
from django.db.models.functions import Coalesce
from rest_framework import viewsets

from ad_statistics.models import Campaign
from ad_statistics.models import Source
from ad_statistics.models import Statistic
from ad_statistics.serializers import CampaignSerializer
from ad_statistics.serializers import DailyStatisticSerializer
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


class DailyStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DailyStatisticSerializer

    def _csv_param(self, name: str) -> List[str]:
        try:
            return self.request.query_params[name].split(',')
        except KeyError:
            return []

    def get_queryset(self):
        query = Statistic.objects.values('date').annotate(
            total_clicks=Sum('clicks'),
            total_impressions=Coalesce(Sum('impressions'), Value(0))).order_by('date')
        campaigns = self._csv_param('campaigns')
        if campaigns:
            query = query.filter(campaign_id__in=campaigns)
        sources = self._csv_param('sources')
        if sources:
            query = query.filter(source_id__in=sources)
        return query
