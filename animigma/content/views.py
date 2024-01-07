from django.contrib.sites import requests
from django.shortcuts import render
from .models import Anime
from django.db.models import F

from django.views.generic import ListView, DetailView, CreateView



def test(request):
    return render(request, 'content/anime.html')


class Home(ListView):
    model = Anime
    template_name = 'content/index.html'
    context_object_name = 'animes'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'classic blog design'
        return context


class AnimeList(ListView):
    template_name = 'content/top.html'
    model = Anime
    context_object_name = 'anime'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GetAnime(DetailView):
    template_name = 'content/single.html'
    model = Anime
    context_object_name = 'anime'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class AnimeByTag(ListView):
    template_name = 'content/index.html'
    context_object_name = 'animes'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Anime.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Anime.objects.get(slug=self.kwargs['slug'])
        return context


class Search(ListView):
    template_name = 'content/search.html'
    context_object_name = 'animes'

    def get_queryset(self):
        return Anime.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context
