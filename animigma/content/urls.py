from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('tag/<str:slug>/', AnimeByTag.as_view(), name='tag'),
    path('anime/<str:slug>/', GetAnime.as_view(), name='anime'),
    path('search/', Search.as_view(), name='search'),
    path('top/', AnimeList.as_view(), name='top'),
    path('test', test, name='test'),
]
