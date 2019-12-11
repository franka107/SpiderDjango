from rest_framework import serializers, generics, permissions
from .models import CurrentMovement, PastMovement, Robot, Sensor, Read, Channel
from django.contrib.auth.models import User, Group
from django.contrib import admin
import datetime
admin.autodiscover()



class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Read
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ('username' , 'email' , 'first_name' , 'last_name' , 'password')

    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email= validated_data['email']
        )
        user.is_active = True
        user.set_password(validated_data['password'])
        user.save()
        return user

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
    class Meta:
        model = Robot
        fields = '__all__'

class ChannelSerializer(serializers .ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'




        
 