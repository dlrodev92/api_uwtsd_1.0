from django.db import models
from technology.models import Technology
from tag.models import Tag

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    repo = models.URLField(max_length=500)  
    technologies = models.ManyToManyField(Technology, related_name='projects', blank=True)  
    tags = models.ManyToManyField(Tag, related_name='projects', blank=True)   
    mainImage = models.TextField(max_length=500, blank=True)


    def __str__(self):
        return self.title




