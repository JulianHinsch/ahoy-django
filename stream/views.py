from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout

from .models import WatchItem, ListenItem

def schedule(request):
    context = {
        'watch_items': WatchItem.objects.all(),
        'listen_items': ListenItem.objects.all(),
    }
    return render(request, 'schedule.html', context)

def watch(request, stream_id):
    context = {'watch_item': get_object_or_404(WatchItem, id = stream_id)}
    return render(request, 'watch.html', context)


def listen(request, stream_id):
    context = {'watch_item': get_object_or_404(WatchItem, id = stream_id)}
    return render(request, 'listen.html', context)
