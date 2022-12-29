from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout

from .models import ListenItem

def listen_schedule(request):
    context = {'streams': ListenItem.objects.all()}
    return render(request, 'listen/listen_schedule.html', context)

def listen(request, stream_id):
    context = {'listen_item': get_object_or_404(ListenItem, id = stream_id)}
    return render(request, 'listen/listen.html', context)
