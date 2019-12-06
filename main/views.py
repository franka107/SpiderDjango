from django.shortcuts import render
from rest_framework import viewsets, permissions, serializers, generics
from .serializers import *
from .permissions import IsOwnerOrReadOnly, IsOwnerRobotOrReadOnly
from .models import CurrentMovement, PastMovement, Robot, Sensor
from django.contrib.auth.models import User
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CurrentMovementViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = CurrentMovement.objects.all()
    serializer_class = CurrentMovementSerializer

class PastMovementViewSet(viewsets.ModelViewSet):
    queryset = PastMovement.objects.all()
    serializer_class = PastMovementsSerializer

class RobotViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerRobotOrReadOnly]
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer 

class SensorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class ReadViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Read.objects.all()
    serializer_class = ReadSerializer

class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

