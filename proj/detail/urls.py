from django.urls import path, include
from .views import (Home, 
RetrieveRegion, 
RetrieveProblem,
RetrieveProblems,
CreateRegion, 
CreateMinistries,
CreateProblem,
TestView)

urlpatterns = [
    path('', Home.as_view()),
    path('retrieveRegion/<int:pk>', RetrieveRegion.as_view()),
    path('retrieveProblem/<int:pk>', RetrieveProblem.as_view()),
    path('retrieveProblems/', RetrieveProblems.as_view()),
    path('createRegion/', CreateRegion.as_view()),
    path('createMinistry/', CreateMinistries.as_view()),
    path('createProblem/', CreateProblem.as_view()),
    path('test/', TestView.as_view()),
]