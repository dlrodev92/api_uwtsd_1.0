from django.db import models
from task.models import Task

class Paragraph(models.Model):
    Task = models.ForeignKey(Task, related_name='paragraphs', on_delete=models.CASCADE)
    paragraph = models.TextField()
    order = models.IntegerField()

    def __str__(self):
        return self.paragraph