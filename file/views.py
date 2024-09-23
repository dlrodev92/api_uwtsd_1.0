from rest_framework import viewsets
from .models import Project
from .serializers import FileSerializer
from uwtsd_api.permissions import IsSuperUser

class FileViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsSuperUser]

