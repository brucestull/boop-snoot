from django.contrib import admin
from django.db import models

from .models import Boop


@admin.register(Boop)
class BoopAdmin(admin.ModelAdmin):
    list_display = ['fuzzy_one', 'order']
    list_editable = ['order']

    def get_changeform_initial_data(self, request):
        """
        Override the default initial data to set the order to the highest
        order number + 1
        """
        # Get the initial data from the default method
        initial_data = super().get_changeform_initial_data(request)
        # Get the highest order number
        highest_order = Boop.objects.all().aggregate(
            models.Max('order'))['order__max']
        # Set the order to the highest order number + 1
        initial_data['order'] = (
            highest_order if highest_order is not None else -1) + 1
        # Return the initial data
        return initial_data
