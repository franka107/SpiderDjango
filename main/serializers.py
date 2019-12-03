from rest_framework import serializers
from .models import CurrentMovement, Robot, Sensor

class CurrentMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentMovement
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class RobotSerializer(serializers.ModelSerializer):
    sensors = SensorSerializer(many=True)
    class Meta:
        model = Robot
        fields = '__all__'