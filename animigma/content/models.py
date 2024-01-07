from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']


class Anime(models.Model):
    title_original = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    year = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, verbose_name='Url', unique=True)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    poster_url = models.URLField(null=True, blank=True)
    views = models.IntegerField(default=0)
    rating = models.FloatField(null=True)
    PEGI = models.CharField(max_length=3, default='0+')

    def __str__(self):
        return self.title_original

    def get_absolute_url(self):
        return reverse('anime', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['year']


class Episode(models.Model):
    anime = models.ForeignKey('Anime', related_name='episodes', on_delete=models.CASCADE)
    episode_number = models.IntegerField()
    video_url = models.URLField()


class Favorite(models.Model):
    anime = models.ForeignKey('Anime', related_name='favorites', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)


