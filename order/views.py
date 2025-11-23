from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from .models import Order
from boat.models import Boat
from django.urls import reverse

from .services import send_order_email


class OrderCreateView(CreateView):
    model = Order
    fields = ["boat", "name", "email", "message"]

    def get_success_url(self):
        return reverse("boat:boat_detail", args=[self.kwargs.get("pk")])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["boat"] = get_object_or_404(Boat, pk=self.kwargs.get("pk"))
        return context_data

    def form_valid(self, form):
        obj = form.save()
        send_order_email(obj)
        return super().form_valid(form)
