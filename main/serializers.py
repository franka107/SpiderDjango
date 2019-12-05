from rest_framework import serializers, generics, permissions
from .models import CurrentMovement, PastMovement, Robot, Sensor
from django.contrib.auth.models import User, Group
from django.contrib import admin
import datetime
admin.autodiscover()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ('username' , 'email' , 'first_name' , 'last_name' , 'password')

class CurrentMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentMovement
        fields = '__all__'

    def create(self, validated_data):
        pastmovement = PastMovement(
            robot= validated_data['robot'],
            direction = validated_data['direction'],
        )
        pastmovement.save()
        return CurrentMovement.objects.create(**validated_data)

    def update( self, instance, validated_data):
        pastmovement = PastMovement(
            robot= validated_data['robot'],
            direction = validated_data['direction'],
        )
        pastmovement.save()
        instance.direction = validated_data.get('direction' , instance.direction)
        instance.save()
        return instance

class PastMovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastMovement
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class RobotSerializer(serializers.ModelSerializer):
    #sensors = SensorSerializer(many=True)
    #sensors= serializers.StringRelatedField(many=True)
     
    class Meta:
        model = Robot
        fields = '__all__'

        
 