from django.contrib import admin
from .models import Boop


@admin.register(Boop)
class BoopAdmin(admin.ModelAdmin):
    list_display = ['fuzzy_one', 'order']
    list_editable = ['order']
