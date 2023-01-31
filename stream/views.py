from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Film

def browse(request):
    context = {
        'films': Film.objects.all(),
    }
    return render(request, 'browse.html', context)

def watch(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    context = { 'film': film }
    return render(request, 'watch.html', context)
