from django.db import models
from task.models import Task

class Image(models.Model):
    task = models.ForeignKey(Task, related_name='images', on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    alt = models.CharField(max_length=100)
    imageUrl = models.URLField(max_length=500)

    def __str__(self):
        return self.imageUrl

