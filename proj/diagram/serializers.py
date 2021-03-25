from rest_framework import serializers

from .models import Diagram, Region

class DiagramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diagram
        fields = ['value', 'problem',]

class RegionSerializer(serializers.ModelSerializer):
    diagram = DiagramSerializer(many=True)

    class Meta:
        model = Region
        fields = ['name', 'diagram', ]