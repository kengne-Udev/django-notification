from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_notifications, name='notifications'),
    path('send-notification', views.send_notification, name='notification'),
    path('', views.snippets, name='snippets'),
    path('snippets', views.snippets, name='snippets'),
]