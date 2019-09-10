from csv import DictReader
from datetime import datetime
from typing import Dict

from django.db import transaction

from ad_statistics.models import Campaign
from ad_statistics.models import Source
from ad_statistics.models import Statistic


class StatisticCSVImporter:
    """CSV string importer.

    Expects the following format (Impressions are optional):
    Date,Datasource,Campaign,Clicks,Impressions
    30.01.2019,Acme corp,Milk,1,
    """

    def __init__(self):
        self.campaigns = {}
        self.sources = {}

    @staticmethod
    def _cached_foreign_instance(cache: Dict, class_, name: str):
        try:
            return cache[name]
        except KeyError:
            obj, created = class_.objects.get_or_create(name=name)
            cache[name] = obj
            return obj

    def _to_model(self, item: Dict):
        statistic = Statistic(
            date=datetime.strptime(item['Date'], '%d.%m.%Y').date(),
            campaign=self._cached_foreign_instance(self.campaigns, Campaign, item['Campaign']),
            source=self._cached_foreign_instance(self.campaigns, Source, item['Datasource']),
            clicks=int(item['Clicks']))
        try:
            statistic.impressions = int(item['Impressions'])
        except ValueError:
            pass
        return statistic

    @transaction.atomic
    def load(self, csv: str):
        items = []
        for raw_item in DictReader(csv.splitlines()):
            items.append(self._to_model(raw_item))
        Statistic.objects.bulk_create(items)
