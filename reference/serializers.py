from .models import Reference 
from rest_framework import serializers

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id', 'text', 'project', 'link', 'accessDate']
