from django.db import models
from django.contrib.auth.models import User
# Create your models here.

MOVEMENTS_CHOICES = [
    ( 'Right', 'Derecha' ),
    ( 'Left' , 'Izquierda'),
    ( 'Front' , 'Avanzar'),
    ( 'Back' , 'Retroceder'),
    ( 'Stop' , 'Parar')
]


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/sensors', null=True,  default = 'images/sensors/default.png')

    def __str__(self):
        return self.name

class Robot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_joined = models.DateField(auto_now_add = True)
    robot_type = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'images/robots', null=True,  default = 'images/robots/defaultrobot.png')

    def __str__(self):
        return self.name

class SensorInstance(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk) + ' - ' + self.sensor.name + ' - ' + self.robot.name

class Read(models.Model):
    sensorinstance = models.ForeignKey(SensorInstance, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
    field1 = models.CharField(max_length= 100, null= True)
    field2 = models.CharField(max_length= 100, null= True)
    field3 = models.CharField(max_length= 100, null= True)


    def __str__(self):
       return str(self.pk) + ' - ' +self.sensorinstance.sensor.name + ' - ' + self.sensorinstance.robot.name

        
class CurrentMovement(models.Model):
    robot = models.OneToOneField( Robot, primary_key = True,  on_delete=models.CASCADE)
    direction = models.CharField(max_length = 30, choices = MOVEMENTS_CHOICES, default= 'Front')

class PastMovement(models.Model):
    robot = models.ForeignKey( Robot, on_delete=models.CASCADE)
    direction = models.CharField(max_length = 30, choices = MOVEMENTS_CHOICES)
    runtime_date = models.DateTimeField(auto_now_add = True)
    duration = models.IntegerField(null = True)