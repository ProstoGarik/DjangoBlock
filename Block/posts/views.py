from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from posts.forms import PostForm, UserForm
from posts.models import Post


def post(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'title': 'Posts', 'posts': posts})


@login_required
def create(request: HttpRequest) -> HttpResponseRedirect | HttpResponse | None:
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(
                title = form.cleaned_data['title']
                text=form.cleaned_data['text']
                author=request.user
            )
            return redirect('posts-list')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'error': 'Все поля обязательные'})

    form = PostForm()
    return render(request, 'posts/create.html', {'form': form})


def show(request: HttpRequest, post_id: int) -> HttpResponse:
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post.show.html', {'post': post})

def update(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
            return HttpResponseForbidden('У вас нет прав на изменение')

    
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('posts-list')
    else:
        form = PostForm(initial=(
            'title': post.title,
            'text': post.text,
        ))
    return render(request, 'posts/edit.html', {'post': post})

def delete(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
    return redirect('posts-list')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/about.html', {'title': 'About us'})

@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/profile.html', {'user': request.user})

@login_required
def sing_out(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('login')
