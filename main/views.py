from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CurrentMovementSerializer
from .models import CurrentMovement

# Create your views here.

class CurrentMovementViewSet(viewsets.ModelViewSet):
    queryset = CurrentMovement.objects.all()
    serializer_class = CurrentMovementSerializer