from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

from posts.forms import PostForm
from posts.models import Post

def posts(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'title': 'Посты', 'posts': posts}) 

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/about.html', {'title': 'О сайте', 'content': "About page!"}) 

def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Login page") 

def create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            Post.objects.create(
                title = form.cleaned_data['title'],
                text=form.cleaned_data['text']
            )
            return redirect('posts')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})

def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Login page!')