from django.urls import path, include
from .views import (
    Home,
    RetrieveDiagram,
    DiagramView,
    CreateDiagramView
    )

urlpatterns = [
    path('', Home.as_view()),
    path('diagram/<int:pk>/', RetrieveDiagram.as_view()),
    path('diagram/', DiagramView.as_view()),
    path('createDiagram/', CreateDiagramView.as_view()),
]
