from django.contrib.auth import views as auth_views
from django.urls import path

from posts import views

urlpatterns = [
    path('posts/', views.post, name='posts-list'),
    path('posts/create', views.create, name='posts-create'),
    path('posts/<int:post_id>/update', views.update, name='posts-update'),
    path('posts/<int:post_id>/delete', views.update, name='posts-delete'),
    path('posts/<int:post_id>/', views.show, name='posts-show'),
    path('about/', views.about, name='about'),
]
