from django.urls import path

from .apps import OrderConfig

app_name = OrderConfig.name
from . import views

urlpatterns = [
    path("create/<int:pk>/", views.OrderCreateView.as_view(), name="order_create"),
]
