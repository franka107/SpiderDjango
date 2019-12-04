from rest_framework import serializers

from .models import *


import datetime


class CurrentMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentMovement
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class ValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = '__all__'


class ReadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Read
        fields = '__all__'


    def create(self, validated_data):
        pastmovement = PastMovement(
            robot= validated_data['robot'],
            direction = validated_data['direction'],
            runtime_date = datetime.datetime.now()
        )
        pastmovement.save()

        return CurrentMovement.objects.create(**validated_data)

    def update( self, instance, validated_data):

        if(PastMovement.objects.count() > 0):
            lastpastmovement = PastMovement.objects.all().last()
            lastruntime = lastpastmovement.runtime_date.replace(tzinfo=None)
            currentruntime =  datetime.datetime.now()
            duration = currentruntime - lastruntime
            lastpastmovement.duration = int(duration.total_seconds())
            lastpastmovement.save()

        pastmovement = PastMovement(
            robot= validated_data['robot'],
            direction = validated_data['direction'],
            runtime_date = datetime.datetime.now()
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

        
