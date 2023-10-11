from django.shortcuts import render, redirect
from .models import Boop
from django.shortcuts import get_object_or_404


def boop_list_view(request):
    boops = Boop.objects.all()
    return render(request, 'boop_list.html', {'boops': boops})


def move_up(request, boop_id):
    boop = get_object_or_404(Boop, id=boop_id)
    previous_boop = Boop.objects.filter(order__lt=boop.order).last()

    if previous_boop:
        boop.order, previous_boop.order = previous_boop.order, boop.order
        boop.save()
        previous_boop.save()

        # Reorder the remaining Boop objects to maintain continuous order
        # values
        for index, remaining_boop in enumerate(Boop.objects.all()):
            remaining_boop.order = index
            remaining_boop.save()

    return redirect('boop_list')


def delete_boop(request, boop_id):
    boop = get_object_or_404(Boop, id=boop_id)
    boop.delete()

    # Reorder the remaining Boop objects
    for index, remaining_boop in enumerate(Boop.objects.all()):
        remaining_boop.order = index
        remaining_boop.save()

    return redirect('boop_list')
