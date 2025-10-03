from django.db import models
from users.models import User

class Note(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=512)
    created = models.DateTimeField("Created")
    updated = models.DateTimeField("Updated")
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line