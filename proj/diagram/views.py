from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView,
    CreateAPIView,
)

from.models import (
    Diagram,
    DiagramElement
)

from .serializers import (
    DiagramSerializer,
    DiagramElementSerializer,
)

from loguru import logger

class Home(APIView):
    def get(self, request):
        data = {"message": "hello world!"}
        return Response(data)

class RetrieveDiagramElement(RetrieveAPIView):
    queryset = DiagramElement.objects.all()
    serializer_class = DiagramElementSerializer

class RetrieveDiagram(RetrieveAPIView):
    queryset = Diagram.objects.all()
    serializer_class = DiagramSerializer

class DiagramView(APIView):
    def get(self, request):
        data = Diagram.objects.all()
        seri = DiagramSerializer(data, many=True)
        return Response(seri.data)

class CreateDiagramView(CreateAPIView):
    serializer_class = DiagramSerializer