from django.urls import path
from . import views

urlpatterns = [
    path('', views.boop_list_view, name='boop_list'),
    path('<int:boop_id>/move-up/', views.move_up, name='move_up'),
    path('<int:boop_id>/delete/', views.delete_boop, name='delete_boop'),
]
