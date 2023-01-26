import csv
from django.core.management.base import BaseCommand
from main.models import *

class Command(BaseCommand):
    help = 'Import data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file'], 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                models.objects.create(
                    name=row['name'],
                    email=row['email'],
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV.'))