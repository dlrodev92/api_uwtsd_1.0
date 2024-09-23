from rest_framework import viewsets
from .models import Technology
from .serializers import TechnologySerializer
from uwtsd_api.permissions import IsSuperUser

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [IsSuperUser]

