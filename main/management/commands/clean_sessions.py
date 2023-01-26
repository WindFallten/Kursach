from django.core.management.base import BaseCommand
from django.contrib.sessions.models import Session
from datetime import timedelta
from django.utils import timezone


class Command(BaseCommand):
    help = 'Clears expired sessions older than a week'

    def handle(self, *args, **options):
        one_week_ago = timezone.now() - timedelta(weeks=1)
        Session.objects.filter(expire_date__lt=one_week_ago).delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared expired sessions.'))