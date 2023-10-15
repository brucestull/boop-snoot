from django.contrib import admin
from django.db import models

from .models import Boop

from django.contrib.admin.actions \
    import delete_selected as delete_selected_original


def delete_selected(modeladmin, request, queryset):
    """
    This function is called when the delete_selected action is triggered.

    We override the default delete_selected function to call our custom
    `reorder_all` function if the model is a `Boop`.
    """
    delete_selected_original(modeladmin, request, queryset)
    if modeladmin.model == Boop:
        Boop.reorder_all()


@admin.register(Boop)
class BoopAdmin(admin.ModelAdmin):
    list_display = ['fuzzy_one', 'order']
    # Allow the order field to be edited in the admin list view
    list_editable = ['order']
    # The `actions` attribute is a list of functions that will be called when
    # the action is triggered. The `delete_selected` function is the default
    # delete action. We override it here to call our custom `delete_selected`
    # function after the default one is called.
    actions = [delete_selected]

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

    def delete_model(self, request, obj):
        super().delete_model(request, obj)
        Boop.reorder_all()
