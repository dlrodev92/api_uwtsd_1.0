from rest_framework import viewsets
from .models import Project
from .serializers import TaskSerializer
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = TaskSerializer

