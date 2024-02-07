from django.shortcuts import redirect, render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def get_notifications(request):
    return render(request, 'notification/index.html', {})

def snippets(request):
    return render(request, 'snippets/table.html', {})


def send_notification(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'public_room',
            {
                "type": "send_notification",
                "message": email
            }
        )
        return redirect('snippets')