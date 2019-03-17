from csv import DictReader

from django.core.management.base import BaseCommand
import csv
from csvReader.models import CsvData

class Command(BaseCommand):
    help = "Load data from csvDjango.csv into our CsvData model"
    def handle(self, *args, **options):

        with open(('./csvDjango.csv')) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                _, created = CsvData.objects.get_or_create(
                    processName = row[0],
                    processId = row[1],
                    )
