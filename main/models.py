from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

class Robot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_joined = models.DateField()
    robot_type = models.CharField(max_length = 50)
    sensors = models.ManyToManyField(Sensor)

    def __str__(self):
        return self.name

class Read(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
       return str(self.pk) + ' - ' +self.sensor.name + ' - ' + self.robot.name

class Value(models.Model):
    read = models.ForeignKey(Read,  on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return  self.read
class Current_movement(models.Model):
    robot = models.OneToOneField( Robot, on_delete=models.CASCADE)
    direction = models.CharField(max_length = 30)

class Past_movement(models.Model):
    robot = models.ForeignKey( Robot, on_delete=models.CASCADE)
    direction = models.CharField(max_length = 30)
    runtime_date = models.DateTimeField() 