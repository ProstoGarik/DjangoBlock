from django.urls import path

from . import views

urlpatterns = [
    path("", views.notes, name="note-list"),
    path("create", views.create, name="note-create"),
    path("edit/<int:id>", views.edit, name="note-edit"),
    path("delete/<int:id>", views.delete, name="note-delete"),
]