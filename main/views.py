from django.shortcuts import render
from rest_framework import viewsets, permissions, serializers, generics
from .serializers import *
from .models import CurrentMovement, PastMovement, Robot, Sensor
from django.contrib.auth.models import User
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentMovementViewSet(viewsets.ModelViewSet):
    permissions_classes = [permissions.AllowAny]
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

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
