from django.db import models


class Boop(models.Model):
    fuzzy_one = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        # if the object is new and doesn't have an order yet
        if not self.pk and not hasattr(self, 'order'):
            highest_order = Boop.objects.all().aggregate(
                models.Max('order'))['order__max']
            self.order = (
                highest_order if highest_order is not None else -1) + 1
        super(Boop, self).save(*args, **kwargs)

    @classmethod
    def reorder_all(cls):
        for index, boop in enumerate(cls.objects.all()):
            boop.order = index
            boop.save()
