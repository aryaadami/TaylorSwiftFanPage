from django.contrib import admin
from .models import Songs, Albums

@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ['album', 'length', 'collab']
    list_filter = ['album', 'rating', 'collab']
    search_fields = ['title', 'album']
    prepopulated_fields = {'slug':('album', 'title')}
    ordering = ['title', 'length', 'rating']

@admin.register(Albums)
class AlbumsAdmin(admin.ModelAdmin):
    search_fields = ['title']
    ordering = ['publish']
