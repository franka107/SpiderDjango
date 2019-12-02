from rest_framework import serializers
from .models import CurrentMovement

class CurrentMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentMovement
        fields = '__all__'