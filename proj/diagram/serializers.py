from rest_framework import serializers

from .models import (
    Problem,
    Ministry,
    ProblemCluster,
    Diagram, 
    )

class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = ['name']

class MinistrySerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many=True)

    class Meta:
        model = Ministry
        fields = ['name', 'problems', ]

class ProblemClusterSerializer(serializers.ModelSerializer):
    ministries = MinistrySerializer(many=True)

    class Meta:
        model =  ProblemCluster
        fields = ['name', 'ministries', ]

class DiagramSerializer(serializers.ModelSerializer):
    problemcluster = ProblemClusterSerializer()

    class Meta:
        model = Diagram
        fields = ['value', 'problemcluster',]

"""
class ServicesSerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many=True)

    class Meta:
        model = Services
        fields = ['name', 'problems']
"""