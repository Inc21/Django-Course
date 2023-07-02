from rest_framework import serializers
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Project serializer
    """
    class Meta:
        """
        meta
        """
        model = Project
        fields = '__all__'
