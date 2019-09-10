from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Source(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Statistic(models.Model):
    date = models.DateField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    clicks = models.IntegerField()
    impressions = models.IntegerField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['date', 'campaign', 'source'], name='unique_daily_campaign_sources')]
