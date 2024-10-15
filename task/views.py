from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from uwtsd_api.permissions import IsSuperUser

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    

