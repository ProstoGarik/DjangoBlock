from django.db import models
from myusers.models import User

class Post(models.Model):
    title = models.CharField(
        max_length=100,
    )
    content = models.TextField()
    author = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    author = models.ForeignKey(
        to=User,
        verbose_name='Автор Поста',
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
