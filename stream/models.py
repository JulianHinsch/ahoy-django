from django.db import models

class Film(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    src = models.CharField(max_length=500)
    thumbnail_src = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.title

