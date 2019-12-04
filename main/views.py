from django.shortcuts import render
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import *
from .models import *
from .models import Value
import pudb;



# Create your views here.

class CurrentMovementViewSet(viewsets.ModelViewSet):
    queryset = CurrentMovement.objects.all()
    serializer_class = CurrentMovementSerializer



class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Probando la api!'}
        return Response(content)


# we must to give the sensor's name attribute
# example: http://localhost:9090/api/temperaturas/?sensor=temperatura1
class RecordsViewSet(APIView):
    def get(self, request):
        sensor_name = self.request.query_params.get('sensor')  # captura el parametro enviado en la petición
        sensor = Sensor.objects.get(name=sensor_name)  # busca el sensor con el nombre del parametro
        # pudb.set_trace()
        reads = Read.objects.filter(sensor=sensor)  # busca las lecturas realizadas por el sensor
        my_dictionary = {}
        for i in range(len(reads)):
            dict2 = {}
            id_read = str(Value.objects.filter(read=reads[i])[0].read.id)
            sensor_name2 = str(Value.objects.filter(read=reads[i])[0].read.sensor.name)
            valor_read = Value.objects.filter(read=reads[i])[0].value

            dict2[sensor_name2] = valor_read
            my_dictionary[id_read] = dict2  # puebla el diccionario a responder

        return Response(my_dictionary)

class PastMovementViewSet(viewsets.ModelViewSet):
    queryset = PastMovement.objects.all()
    serializer_class = PastMovementsSerializer

class RobotViewSet(viewsets.ModelViewSet):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer 

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

