from django.shortcuts import render, redirect
# from .forms import RegisterForm, LoginForm
from .forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserLoginForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hashuser

def register(request):
    redirect_url = getattr(settings, "LOGIN_REDIRECT_URL", None)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email, password=raw_password)
            if user is not None:
                auth_login(request, user)
            else:
                print("user is not authenticated")
            return redirect(redirect_url)
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})



def login(request):
    redirect_url = getattr(settings, "LOGIN_REDIRECT_URL", None)
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        print(form.is_valid())
        # print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect(redirect_url)
    else:
        form = CustomUserLoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    redirect_url = getattr(settings, "LOGOUT_REDIRECT_URL", None)
    auth_logout(request)
    return redirect(redirect_url)

def change_password(request):
    redirect_url = getattr(settings, "LOGOUT_REDIRECT_URL", None)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {
        'form': form
    })