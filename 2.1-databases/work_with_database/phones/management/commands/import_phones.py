import csv
from django.core.management.base import BaseCommand
from phone.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('phones.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                phone = Phone(
                    id=row['id'],
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=(row['lte_exists'] == 'True'),
                    slug=slugify(row['name'])
                )
                phone.save()
