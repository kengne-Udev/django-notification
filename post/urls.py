from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post-data', views.post_data, name='post-data'),
    path('chat', views.index, name='chat'),
    path("chat/<str:room_name>/", views.room, name="room"),
]
