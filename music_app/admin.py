from django.contrib import admin
from .models import Song, History, LikedSong, Singer, Playlist
# Register your models here.

class SongAdmin(admin.ModelAdmin):
    list_display=('song_id','name')
admin.site.register(Song,SongAdmin)
admin.site.register(History)
admin.site.register(LikedSong)
admin.site.register(Singer)
admin.site.register(Playlist)