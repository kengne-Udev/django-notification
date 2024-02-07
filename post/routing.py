from django.urls import path

from . import consumers
from notification.consumers import NotificationConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
    path('ws/notify/', NotificationConsumer.as_asgi()),
]