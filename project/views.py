from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from uwtsd_api.permissions import IsSuperUser

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsSuperUser]

