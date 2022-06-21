from django.contrib import admin
from .models import Anime


class AnimeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'temporada', 'status', 'usuario')

admin.site.register(Anime, AnimeAdmin)