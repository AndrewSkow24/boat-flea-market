from django.urls import path
from .apps import BoatConfig
from . import views

app_name = BoatConfig.name

urlpatterns = [
    path("", views.BoatListView.as_view(), name="boat_list"),
    path("<int:pk>/", views.BoatDetailView.as_view(), name="boat_detail"),
]
