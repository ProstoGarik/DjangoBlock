from django.contrib.auth import views as auth_views
from django.urls import path

from myusers import views

urlpatterns = [
    path('login/', views.login_view, name='users-login'),
    #path('register/', views.login_view, name='users-register'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]
