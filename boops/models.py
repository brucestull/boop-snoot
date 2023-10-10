from django.db import models


class Boop(models.Model):
    fuzzy_one = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
