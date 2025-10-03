from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Note
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def notes(request):
    # Only get notes for the current user
    notes = Note.objects.filter(user=request.user)
    return render(request, "notes.html", {'notes': notes})

@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        # Create note with current user
        Note.objects.create(
            title=title,
            content=content,
            created=timezone.now(),
            updated=timezone.now(),
            user=request.user  # Add current user
        )
        return redirect('note-list')
    
    return render(request, 'create.html')

@login_required
def edit(request, id):
    # Only allow editing notes that belong to current user
    note = get_object_or_404(Note, id=id, user=request.user)
    
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.updated = timezone.now()
        note.save()
        return redirect('note-list')
    
    return render(request, 'edit.html', {'note': note})

@login_required
def delete(request, id):
    # Only allow deleting notes that belong to current user
    note = get_object_or_404(Note, id=id, user=request.user)
    note.delete()
    return redirect('note-list')