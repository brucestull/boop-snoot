from boops.models import Boop


from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create some boops"

    def handle(self, *args, **kwargs):
        # Create 10 boops
        for i in range(10, 21):
            boop = Boop.objects.create(fuzzy_one=f"Boop {i}", order=i)
            Boop.reorder_all()
            boop.save()

        self.stdout.write(self.style.SUCCESS("Created Some Boops!?"))


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
