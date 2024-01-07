from django.db import models
from content.models import Anime


class Comment(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_at']


class CommentReply(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-created_at']
