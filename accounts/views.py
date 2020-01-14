from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.models import Customer
from accounts.forms import RegisterForm
from accounts.utils import old_enough


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = authenticate(username=username,
                                password=password, email=email)
            login(request, user)
        else:
            return render(request, 'register.html', {'form': form})
        return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
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
