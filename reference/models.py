from django.db import models
from project.models import Project

# Create your models here.
class Reference(models.Model):
    project = models.ForeignKey( Project, related_name='references', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
    accessDate = models.CharField(max_length=100)
    
    def __str__(self):
        return self.text