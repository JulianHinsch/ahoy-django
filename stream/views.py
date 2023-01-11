from django.shortcuts import render
from datetime import datetime

from .models import VideoItem, AudioItem

def schedule(request):
    context = {
        'video_items': VideoItem.objects.filter(start_time__date = datetime.today()),
        'audio_items': AudioItem.objects.filter(start_time__date = datetime.today()),
    }
    return render(request, 'schedule.html', context)

def watch(request):
    try:
        current_item = VideoItem.objects.filter(start_time__gte = datetime.now()).earliest('start_time')
    except VideoItem.DoesNotExist:
        current_item = None
    context = {'video_item': current_item }
    return render(request, 'watch.html', context)


def listen(request):
    try:
        current_item = AudioItem.objects.filter(start_time__gte = datetime.now()).earliest('start_time')
    except AudioItem.DoesNotExist:
        current_item = None
    context = {'audio_item': current_item }
    return render(request, 'listen.html', context)
