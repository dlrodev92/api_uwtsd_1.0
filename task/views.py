from rest_framework import viewsets
from .models import Project
from .serializers import TaskSerializer
from uwtsd_api.permissions import IsSuperUser

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsSuperUser]

