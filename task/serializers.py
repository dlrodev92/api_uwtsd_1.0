from rest_framework import serializers
from .models import Task
from subtitle.serializers import SubtitleSerializer
from paragraph.serializers import ParagraphSerializer


class TaskSerializer(serializers.ModelSerializer):
    
    subtitles = SubtitleSerializer(many=True, read_only=True)
    paragraphs = ParagraphSerializer(many=True, read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'project', 'name', 'order', 'subtitles', 'paragraphs',]
