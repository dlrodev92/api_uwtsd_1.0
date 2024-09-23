from django.db import models
from project.models import Project

class File(models.Model):
    project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    fileUrl = models.URLField(max_length=500)

    def __str__(self):
        return self.name
    