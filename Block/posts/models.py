from django.db import models

class Post(models.Model):
    title = models.CharField(
        verbose_name= 'заголовок',
        max_length = 128,
    )

    text = models.TextField(
        verbose_name= 'Текст',
        max_length = 512,
    )

    created = models.DateTimeField(
        verbose_name= 'Создано',
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        verbose_name= 'Изменено',
        auto_now=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'