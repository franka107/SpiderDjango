from django.shortcuts import render
from rest_framework import viewsets, permissions, serializers, generics, views
from .serializers import *
from django.http import Http404
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly, IsOwnerRobotOrReadOnly
from .models import CurrentMovement, PastMovement, Robot, Sensor
from django.contrib.auth.models import User
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from rest_framework import status


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]

    #permission_classes = [permissions.IsAdminUser, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    

class ChannelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class CurrentMovementViewSet(viewsets.ModelViewSet):
    #permission_classes = [IsOwnerOrReadOnly]
    permission_classes = [permissions.AllowAny]
    queryset = CurrentMovement.objects.all()
    serializer_class = CurrentMovementSerializer

class PastMovementViewSet(viewsets.ModelViewSet):
    queryset = PastMovement.objects.all()
    serializer_class = PastMovementsSerializer

class RobotViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerRobotOrReadOnly, permissions.IsAuthenticatedOrReadOnly ]
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

class ReadList(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Read.objects.filter(sensorinstance = pk)
        except Read.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        reads = self.get_object(pk)
        serializer = ReadSerializer(reads, many=True)
        return Response(serializer.data)

""" class DataList(views.APIView):
    permission_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
 """
    





