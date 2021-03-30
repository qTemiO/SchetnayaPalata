from rest_framework import serializers

from .models import (
    Problem,
    Ministry,
    ProblemCluster,
    DiagramElement, 
    Diagram,
    )

class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = ['prob_name']

class MinistrySerializer(serializers.ModelSerializer):
    problems = ProblemSerializer(many=True)

    class Meta:
        model = Ministry
        fields = ['min_name', 'problems', ]

class ProblemClusterSerializer(serializers.ModelSerializer):
    ministries = MinistrySerializer(many=True)

    class Meta:
        model =  ProblemCluster
        fields = ['probClus_name', 'ministries', ]

class DiagramElementSerializer(serializers.ModelSerializer):
    problemcluster = ProblemClusterSerializer()

    class Meta:
        model = DiagramElement
        fields = ['value', 'problemcluster',]

class DiagramSerializer(serializers.ModelSerializer):
    columns = DiagramElementSerializer(many=True)

    class Meta:
        model = Diagram
        fields = ['columns']

    def create(self, validated_data):
        
        diagram = Diagram.objects.create()
        diagramElements = validated_data.pop('columns')
        
        for diagramElement in diagramElements:
            problemcluster = diagramElement.pop('problemscluster')
            diagramElement = DiagramElement.objects.create(value=diagramElement['value'])

            for problem in problemcluster:
                ministries = problem.pop('ministries')
                problem = ProblemCluster.objects.create(probClus_name=problem['probClus_name'])

                for ministry in ministries:
                    problems = ministry.pop('problems')
                    ministry, created = Ministries.objects.get_or_create(min_name=ministry['min_name'])

                    for prob in problems:
                        prob, created = Problem.objects.get_or_create(prob_name=prob['prob_name'])
                
                        ministry.services.add(prob)
                
                    problem.ministries.add(ministry)

                diagramElement.problemcluster.add(problem)
        
            diagram.columns.add(diagramElement)

        return diagram
