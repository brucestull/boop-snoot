import time

from django.core.management.base import BaseCommand

from boops.models import Boop


class Command(BaseCommand):
    help = "Create some boops"

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--boops", type=int, help="Number of boops to create", default=10
        )

    def handle(self, *args, **kwargs):
        number_of_boops = kwargs.get("boops", 10)

        self.stdout.write("Creating Boops...")
        for i in range(1, number_of_boops + 1):
            boop = Boop.objects.create(fuzzy_one=f"Boop {i}", order=i)
            self.stdout.write(self.style.SUCCESS(f"Created Boop {i}"))
            boop.save()
            self.stdout.write(self.style.SUCCESS(f"Saved Boop {i}"))
            time.sleep(0.5)

        Boop.reorder_all()
        self.stdout.write(
            self.style.SUCCESS(f"Reordered Boops after creating Boop {i}")
        )
        self.stdout.write(self.style.SUCCESS(f"Created {number_of_boops} Boops."))
