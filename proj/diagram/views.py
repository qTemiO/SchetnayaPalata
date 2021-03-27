from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
        GenericAPIView,
        RetrieveAPIView,
    )

from.models import Diagram
from .serializers import (
    DiagramSerializer,
)

from loguru import logger

class Home(APIView):
    def get(self, request):
        data = {"message": "hello world!"}
        return Response(data)

class RetrieveDiagram(RetrieveAPIView):
    queryset = Diagram.objects.all()
    serializer_class = DiagramSerializer

class DiagramView(APIView):
    def get(self, request):
        data = Diagram.objects.all()
        seri = DiagramSerializer(data, many=True)
        return Response(seri.data)
