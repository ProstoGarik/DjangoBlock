from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User

from posts.forms import PostForm, UserForm
from posts.models import Post

def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('post-list')
            else:
                return render(request, 'login.html', {'errors': 'Неверные имя пользователя и/или пароль'})
    else:
        form = UserForm()
    return render(request, 'login.html', {'title': 'Login', 'form': form})

def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('login')

@login_required
def profile_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/profile.html', {'user': request.user})

def refister_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Пользователь с таким именем уже существует')
            else:
                User.objects.create_user(username=username, password=password)
                return redirect('users-login')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'html': form})