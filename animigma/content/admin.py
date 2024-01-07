from django.contrib import admin

from .models import *


class AnimeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title_original',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Anime, AnimeAdmin)
admin.site.register(Episode)
admin.site.register(Favorite)
admin.site.register(Tag, TagAdmin)