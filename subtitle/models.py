from django.db import models
from task.models import Task

class Subtitle(models.Model):
    task = models.ForeignKey(Task, related_name='subtitles', on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=100)
    order = models.IntegerField()

    def __str__(self):
        return self.subtitle
