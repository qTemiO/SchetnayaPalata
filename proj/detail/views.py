from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
        GenericAPIView,
        RetrieveAPIView,
        CreateAPIView,
    )

from.models import Region, Problem
from .serializers import (
    MinistriesSerializer,
    ProblemSerializer,
    RegionSerializer,
)

from loguru import logger
# Create your views here.

class Home(APIView):
    def get(self, request):
        return (Response({'data':'welcome to detail VIew!'}))

class RetrieveRegion(RetrieveAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RetrieveProblem(RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class RetrieveProblems(APIView):
    def get(self, request):
        queryset = Problem.objects.all()
        serializer = ProblemSerializer(queryset, many=True)
        return Response(serializer.data)

class CreateRegion(CreateAPIView):
    serializer_class = RegionSerializer

class CreateProblem(CreateAPIView):
    serializer_class = ProblemSerializer

class CreateMinistries(CreateAPIView):
    serializer_class = MinistriesSerializer

class TestView(APIView):
    def post(self, request):
        data = request.POST
        logger.debug(data)
        serializer = RegionSerializer(data=data, many=True)
        logger.debug(serializer)
        if serializer.is_valid():
            return Response({"success": "created successfully"})
        else:
            return Response(serializer.data)