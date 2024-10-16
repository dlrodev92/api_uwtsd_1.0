from rest_framework import serializers
from .models import Project
from task.serializers import TaskSerializer
from reference.serializers import ReferenceSerializer
from technology.models import Technology
from tag.models import Tag
from file.models import File
from file.serializers import FileSerializer



class ProjectSerializer(serializers.ModelSerializer):
    references = ReferenceSerializer(many=True, read_only=True)
    tasks = TaskSerializer(many=True, read_only=True)
    
    technologies = serializers.SlugRelatedField(
        many=True,
        queryset=Technology.objects.all(),
        slug_field='name',
        required=False
    )
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.distinct('name'),
        slug_field='name',
        required=False
    )
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description','mainImage', 'date', 'repo', 'technologies', 'tags', 'files', 'tasks', 'references', 'metatitle']
