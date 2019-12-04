from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CurrentMovementSerializer, RobotSerializer, SensorSerializer, PastMovementsSerializer
from .models import CurrentMovement, PastMovement, Robot, Sensor

# Create your views here.

class CurrentMovementViewSet(viewsets.ModelViewSet):
    queryset = CurrentMovement.objects.all()
    serializer_class = CurrentMovementSerializer

class PastMovementViewSet(viewsets.ModelViewSet):
    queryset = PastMovement.objects.all()
    serializer_class = PastMovementsSerializer

class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer 

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer