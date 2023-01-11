from django.contrib import admin
from .models import AudioItem, VideoItem, AudioPlaylist, VideoPlaylist, AudioPlaylistItem, VideoPlaylistItem

admin.site.register(AudioItem)
admin.site.register(VideoItem)
admin.site.register(AudioPlaylist)
admin.site.register(AudioPlaylistItem)
admin.site.register(VideoPlaylist)
admin.site.register(VideoPlaylistItem)
