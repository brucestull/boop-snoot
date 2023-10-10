from django.urls import path
from . import views

urlpatterns = [
    path('', views.boop_list_view, name='boop_list'),
    path('<int:boop_id>/move-up/', views.move_up, name='move_up'),
]
