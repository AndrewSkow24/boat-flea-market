from boat.models import Boat
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER

from order.models import Order


def send_order_email(order_item):
    send_mail(
        "Заявка на покупку лодки",
        f"{order_item.name} ({order_item.email}) хочет купить вашу лодку {order_item.boat.name}. Вот сообщение: '{order_item.message}'.",
        EMAIL_HOST_USER,
        [order_item.boat.owner.email],
    )
