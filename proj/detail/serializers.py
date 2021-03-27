from rest_framework import serializers

from .models import (
    Services,
    Ministries,
    Problem,
    Region, 
    )
from loguru import logger

class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ['serv_name']

class MinistriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministries
        fields = ['min_name', 'services']

    services = ServicesSerializer(many=True)

    def create(self, validated_data):
        services = validated_data.pop('services')
        ministry = Ministries.objects.create(**validated_data)

        for service in services:
            service, created = Services.objects.get_or_create(serv_name=service['serv_name'])
            ministry.services.add(service)
        return ministry

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['prob_name', 'ministries']
    
    ministries = MinistriesSerializer(many=True)

    def create(self, validated_data):
        ministries = validated_data.pop('ministries')

        if (Problem.objects.filter(prob_name=validated_data['prob_name'])):
            problem = Problem.objects.get(prob_name=validated_data.prob_name)
        else:
            problem = Problem.objects.create(**validated_data)

        for ministry in ministries:
            services = ministry.pop('services')
            ministry, created = Ministries.objects.get_or_create(min_name=ministry['min_name'])

            for service in services:
                service, created = Services.objects.get_or_create(serv_name=service['serv_name'])
                ministry.services.add(service)

            problem.ministries.add(ministry)
        return problem

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['reg_name', 'problems']

    problems = ProblemSerializer(many=True)
    
    def create(self, validated_data):
        problems = validated_data.pop('problems')
        
        region = Region.objects.create(reg_name=validated_data['reg_name'])

        for problem in problems:
            ministries = problem.pop('ministries')
            
            problem = Problem.objects.create(prob_name=problem['prob_name'])

            for ministry in ministries:
                services = ministry.pop('services')
                ministry, created = Ministries.objects.get_or_create(min_name=ministry['min_name'])

                for service in services:
                    service, created = Services.objects.get_or_create(serv_name=service['serv_name'])
                    ministry.services.add(service)

                problem.ministries.add(ministry)

            region.problems.add(problem)
        
        return region
