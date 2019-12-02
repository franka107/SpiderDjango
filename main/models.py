from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

class Robot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_joined = models.TimeField()
    robot_type = models.CharField(max_length = 50)
    sensors = models.ManyToManyField(Sensor)

class Read(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    date = models.DateField()

class Value(models.Model):
    read = models.ForeignKey(Read,  on_delete=models.CASCADE)
    value = models.IntegerField()

class Current_movements(models.Model):
    robot = models.OneToOneField( Robot, on_delete=models.CASCADE)
    direction = models.CharField(max_length = 30)

class Past_movements(models.Model):
    robot = models.ForeignKey( Robot, on_delete=models.CASCADE)
    direction = models.CharField(max_length = 30)
    runtime_date = models.DateTimeField() 