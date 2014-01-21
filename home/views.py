from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def enter(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'index.html', {'username': request.user.username})


def log_out(request):
    logout(request)
    return redirect('enter')
