from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=512)
    created = models.DateTimeField("Created")
    updated = models.DateTimeField("Updated")