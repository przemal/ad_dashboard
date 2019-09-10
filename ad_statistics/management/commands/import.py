import requests
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from ad_statistics.management.commands._importer import StatisticCSVImporter


class Command(BaseCommand):
    help = 'Import statistics to the applications database.'

    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str, help='Source CSV URL(s)')

    def handle(self, *args, **options):
        for url in options['urls']:
            try:
                response = requests.get(url)
                response.raise_for_status()
            except requests.exceptions.RequestException:
                self.stdout.write(f'Failed to import {url}')
            else:
                self.stdout.write(f'Importing {url}..', ending=' ')
                # TODO wrap all exceptions
                try:
                    StatisticCSVImporter().load(response.text)
                except IntegrityError:
                    self.stdout.write('FAILED (integrity error)')
                except KeyError:
                    self.stdout.write('FAILED (missing column)')
                else:
                    self.stdout.write('OK')
