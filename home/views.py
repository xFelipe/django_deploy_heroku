from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout


# Create your views here.
def home(request):
    return render(request, 'home.html')


def logout(request):
    django_logout(request)
    return redirect('home')
