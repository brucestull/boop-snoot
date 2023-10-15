from typing import Any
from django import forms
from .models import Boop
from django.db import models


class BoopForm(forms.ModelForm):
    class Meta:
        model = Boop
        fields = ["fuzzy_one"]

    def save(self, commit: bool = ...) -> Any:
        # if the object is new and doesn't have an order yet
        highest_order = Boop.objects.all().aggregate(models.Max("order"))["order__max"]
        # add one to that number and make it this object's order
        self.order = (highest_order if highest_order is not None else -1) + 1
        # Call the "real" save() method. In other words, call the super class'
        # save() method.
        return super().save(commit)
