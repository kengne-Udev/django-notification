import json
from django.shortcuts import render


def home(request):
    data = [
        {'id': 1, 'name': 'jean', 'description': 'Joviale'},
    ]
    return render(request, 'index.html', {'data': data})


def post_data(request):
    data = []
    id = request.POST.get('id')
    name = request.POST.get('name')
    age = request.POST.get('age')
    description = request.POST.get('description')
    line = {}
    
    line['id'] = id
    line['name'] = name
    line['age'] = age
    line['description'] = description
    data.append(line)
    return render(request, 'snippets/table.html', {'data': data})


def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

