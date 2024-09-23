
from .models import Subtitle
from rest_framework import serializers

class SubtitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtitle
        fields = ['id', 'subtitle', 'order', 'task']

