from rest_framework import viewsets
from .models import Tag
from .serializers import TagSerializer
from uwtsd_api.permissions import IsSuperUser

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsSuperUser]

