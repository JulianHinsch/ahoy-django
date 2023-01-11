from django.db import models

class VideoItem(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    src = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

class AudioItem(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 300)
    src = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

class AudioPlaylist(models.Model):
    title = models.CharField(max_length = 100)
    items = models.ManyToManyField('AudioItem', through='AudioPlaylistItem')
    day_of_week = models.IntegerField(unique=True, verbose_name='Day of Week: Sunday 0 - Saturday 6')
    objects = models.Manager()

    class Meta:
        ordering = ['day_of_week']

    def __str__(self):
        return self.title

class VideoPlaylist(models.Model):
    title = models.CharField(max_length = 100)
    items = models.ManyToManyField('VideoItem', through='VideoPlaylistItem')
    day_of_week = models.IntegerField(unique=True, verbose_name='Day of Week: Sunday 0 - Saturday 6')
    objects = models.Manager()

    class Meta:
        ordering = ['day_of_week']

    def __str__(self):
        return self.title

class VideoPlaylistItem(models.Model):
    video_playlist = models.ForeignKey('VideoPlaylist', on_delete=models.CASCADE)
    video_item = models.ForeignKey('VideoItem', on_delete=models.PROTECT)
    position = models.IntegerField()

    class Meta:
        ordering = ['position']

class AudioPlaylistItem(models.Model):
    audio_playlist = models.ForeignKey('AudioPlaylist', on_delete=models.CASCADE)
    audio_item = models.ForeignKey('AudioItem', on_delete=models.PROTECT)
    position = models.IntegerField()

    def __str__(self):
        return self.audio_playlist.__str__() + " " + self.position.__str__() + ". - " + self.audio_item.__str__()

    class Meta:
        ordering = ['position']
