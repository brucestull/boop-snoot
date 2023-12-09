import time

from django.core.management.base import BaseCommand

from boops.models import Boop


class Command(BaseCommand):
    help = "Create some boops"

    def handle(self, *args, **kwargs):
        # Create 10 boops
        self.stdout.write("Creating Boops...")
        number_of_boops = 10
        for i in range(1, number_of_boops + 1):
            boop = Boop.objects.create(fuzzy_one=f"Boop {i}", order=i)
            self.stdout.write(self.style.SUCCESS(f"Created Boop {i}"))
            Boop.reorder_all()
            self.stdout.write(
                self.style.SUCCESS(f"Reordered Boops after creating Boop {i}")
            )
            boop.save()
            self.stdout.write(self.style.SUCCESS(f"Saved Boop {i}"))
            time.sleep(0.5)

        self.stdout.write(self.style.SUCCESS(f"Created {number_of_boops} Boops."))


# Create 10 boops
# for i in range(10):
#     boop = Boop.objects.create(fuzzy_one=f"Boop {i}")
#     Boop.reorder_all()
#     boop.save()

# boop = Boop.objects.create(fuzzy_one="Boop 1")
# boop.save()
# print(boop.order)

# boop = Boop(fuzzy_one="Boop 2")
# boop.save()
