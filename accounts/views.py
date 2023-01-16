from django.shortcuts import render

from django.shortcuts import render

from .forms import CustomUserCreationForm

from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            u = form.cleaned_data['username']
            p = form.cleaned_data['password1']
            new_user = authenticate(username = u, password = p)
            login(request, new_user)
            return HttpResponseRedirect("/")
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})