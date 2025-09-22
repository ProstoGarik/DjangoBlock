from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from posts.models import Post

def posts(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'title': 'Посты', 'posts': posts}) 

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'posts/about.html', {'title': 'О сайте', 'content': "About page!"}) 

def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Login page") 