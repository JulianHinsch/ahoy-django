from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout

from .models import WatchItem

def watch_schedule(request):
    context = {'streams': WatchItem.objects.all()}
    return render(request, 'watch/watch_schedule.html', context)

def watch(request, stream_id):
    context = {'watch_item': get_object_or_404(WatchItem, id = stream_id)}
    return render(request, 'watch/watch.html', context)
