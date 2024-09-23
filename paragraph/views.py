from rest_framework import viewsets
from .models import  Paragraph
from .serializers import  ParagraphSerializer

class ParagraphViewSet(viewsets.ModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer


