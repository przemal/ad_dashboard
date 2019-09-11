from rest_framework import serializers

from ad_statistics.models import Campaign
from ad_statistics.models import Source
from ad_statistics.models import Statistic


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'


class DailyStatisticSerializer(serializers.ModelSerializer):
    total_clicks = serializers.IntegerField()
    total_impressions = serializers.IntegerField()

    class Meta:
        model = Statistic
        fields = ('date', 'total_clicks', 'total_impressions')
