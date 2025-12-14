# articles/models.py
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])
class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        related_name='comments',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    comment = models.TextField()  # texto do comentário
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:50]

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.article.id)])