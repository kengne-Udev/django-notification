from django.urls import path, include

urlpatterns = [
    path('', include('post.urls')),
    path('notification/', include('notification.urls')),
]
