from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Boop
from .forms import BoopForm


def boop_list_view(request):
    boops = Boop.objects.all()
    form = BoopForm()

    # Check if form is submitted
    if request.method == "POST":
        form = BoopForm(request.POST)
        if form.is_valid():
            new_boop = form.save(commit=False)
            new_boop.save()
            return redirect(
                "boop_list"
            )  # assuming 'boop_list' is the name of the URL pattern for this view

    return render(request, "boop_list.html", {"boops": boops, "form": form})


def move_up(request, boop_id):
    boop = get_object_or_404(Boop, id=boop_id)
    previous_boop = Boop.objects.filter(order__lt=boop.order).last()

    if previous_boop:
        boop.order, previous_boop.order = previous_boop.order, boop.order
        boop.save()
        previous_boop.save()
        Boop.reorder_all()

    return redirect("boop_list")


def delete_boop(request, boop_id):
    boop = get_object_or_404(Boop, id=boop_id)
    boop.delete()
    Boop.reorder_all()
    return redirect("boop_list")
