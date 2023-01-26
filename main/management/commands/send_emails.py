from django.core.management.base import BaseCommand
from django.core.mail import send_mass_mail
from main.models import User

class Command(BaseCommand):
    help = 'Send an email to all users'

    def add_arguments(self, parser):
        parser.add_argument('subject', type=str)
        parser.add_argument('message', type=str)

    def handle(self, *args, **options):
        users = User.objects.all()
        messages = [(options['subject'], options['message'], 'noreply@example.com', [user.email]) for user in users]
        send_mass_mail(messages)
        self.stdout.write(self.style.SUCCESS('Successfully sent email to all users.'))