from django.db import models

class ListenItem(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 300)
    src = models.CharField(max_length=500, verbose_name='Media Source URL')
    date_created = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    objects = models.Manager()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Audio Stream'
        verbose_name_plural = 'Audio Streams'
