from django.shortcuts import render
from datetime import datetime
from django.utils import timezone

from .models import WatchItem, ListenItem

def schedule(request):
    context = {
        'watch_items': WatchItem.objects.filter(start_time__date = datetime.today()),
        'listen_items': ListenItem.objects.filter(start_time__date = datetime.today()),
    }
    return render(request, 'schedule.html', context)

def watch(request):
    try:
        current_item = WatchItem.objects.filter(start_time__gte = timezone.now()).earliest('start_time')
    except WatchItem.DoesNotExist:
        current_item = None
    context = {'watch_item': current_item }
    return render(request, 'watch.html', context)


def listen(request):
    try:
        current_item = ListenItem.objects.filter(start_time__gte = timezone.now()).earliest('start_time')
    except ListenItem.DoesNotExist:
        current_item = None
    context = {'listen_item': current_item }
    return render(request, 'listen.html', context)
