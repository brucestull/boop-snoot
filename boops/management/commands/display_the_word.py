from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Displays the word"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("The Word!?"))
