from rest_framework import viewsets
from .models import  Paragraph
from .serializers import  ParagraphSerializer
from uwtsd_api.permissions import IsSuperUser

class ParagraphViewSet(viewsets.ModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [IsSuperUser]

