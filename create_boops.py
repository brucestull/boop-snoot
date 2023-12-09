from django.core.management.base import BaseCommand

from boops.models import Boop


class Command(BaseCommand):
    help = "Create a bunch of boops"

    def handle(self, *args, **kwargs):
        for i in range(10):
            Boop.objects.create(fuzzy_one=f"Boop {i}")
        Boop.reorder_all()
        self.stdout.write(self.style.SUCCESS("Successfully created boops"))
