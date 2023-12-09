from boops.models import Boop
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Reorder the boops"

    def handle(self, *args, **kwargs):
        Boop.reorder_all()
        self.stdout.write(self.style.SUCCESS("Reordered the Boops!?"))
