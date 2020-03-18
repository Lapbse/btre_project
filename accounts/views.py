from django.shortcuts import render, redirect
from django.contrib import messages


def register(request):
    if request.method == 'POST': #Si procesó el formulario...
        messages.error(request, 'Testing error message')
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST': #Si procesó el formulario...
        # Login user
        return
    else:
        return render(request, 'accounts/login.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def logout(request):
    return redirect('index')