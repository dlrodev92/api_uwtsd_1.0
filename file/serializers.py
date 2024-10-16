
from .models import File
from rest_framework import serializers
from project.models import Project

class FileSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    class Meta:
        model = File
        fields = ['id', 'project', 'name', 'fileUrl']