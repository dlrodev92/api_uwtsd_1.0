from rest_framework import viewsets
from .models import Reference
from .serializers import ReferenceSerializer
from uwtsd_api.permissions import IsSuperUser

class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
  