from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Note
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def notes(request):
    notes = Note.objects.all()
    return render(request, "notes.html", {'notes':  notes })


@login_required
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        Note.objects.create(
            title=title,
            content=content,
            created=timezone.now(),
            updated=timezone.now()
        )
        return redirect('note-list')
    
    return render(request, 'create.html')

@login_required
def edit(request, id):
    note = get_object_or_404(Note, id=id)
    
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.updated = timezone.now()
        note.save()
        return redirect('note-list')
    
    return render(request, 'edit.html', {'note': note})

@login_required
def delete(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('note-list')
