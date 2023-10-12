from django.shortcuts import get_object_or_404, redirect, render

from .models import Boop


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
        Boop.reorder_all()

    return redirect('boop_list')


def delete_boop(request, boop_id):
    boop = get_object_or_404(Boop, id=boop_id)
    boop.delete()
    Boop.reorder_all()
    return redirect('boop_list')
