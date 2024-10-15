from rest_framework import viewsets
from .models import Subtitle
from .serializers import SubtitleSerializer
from uwtsd_api.permissions import IsSuperUser

class SubtitleViewSet(viewsets.ModelViewSet):
    queryset = Subtitle.objects.all()
    serializer_class = SubtitleSerializer
    

