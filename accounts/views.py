from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.forms import RegisterForm, LoginForm


# Create your views here.
def register(request):
    errors = []

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirmed_password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        else:
            errors.appen
        return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'login.html', {'form': form})
