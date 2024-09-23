from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
from uwtsd_api.permissions import IsSuperUser

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsSuperUser]

