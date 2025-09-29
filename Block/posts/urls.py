from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.posts, name="posts"),
    path('posts/create', views.posts, name="create"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
]
