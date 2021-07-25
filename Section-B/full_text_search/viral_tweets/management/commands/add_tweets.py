from django.core.management.base import BaseCommand
from faker import Faker

from ...models import ViralTweet


class Command(BaseCommand):
    help = "Adds tweets to the database"

    def handle(self, *args, **options):
        fake = Faker(['it_IT', 'en_US', 'ar_SA'])

        for _ in range(300):
            print('Populating database ..')
            ViralTweet.objects.create(user_handle='@'+f'{fake.last_name()}', tweet=fake.text())

        print("Populating completed.")