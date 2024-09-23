from django.db import models
from project.models import Project

class Task(models.Model):
    project = models.ForeignKey( Project, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    order = models.IntegerField(null=True)

    def __str__(self):
        return self.title
