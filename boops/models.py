from django.db import models


class Boop(models.Model):
    fuzzy_one = models.CharField(max_length=100)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]

    def save(self, *args, **kwargs):
        # if the object is new and doesn't have an order yet
        if not self.pk and not hasattr(self, "order"):
            # get the highest order number
            highest_order = Boop.objects.all().aggregate(models.Max("order"))[
                "order__max"
            ]
            # add one to that number and make it this object's order
            self.order = (highest_order if highest_order is not None else -1) + 1
        # Call the "real" save() method. In other words, call the super class'
        # save() method.
        super(Boop, self).save(*args, **kwargs)

    @classmethod
    def reorder_all(cls):
        # enumerate through all the objects and get an index number
        for index, boop in enumerate(cls.objects.all()):
            # set the order to the index number
            boop.order = index
            # save the object with the assigned order
            boop.save()

    def __str__(self):
        return self.fuzzy_one + " " + str(self.order) + " " + str(self.pk)
