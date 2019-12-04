from rest_framework import serializers
from .models import *


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

