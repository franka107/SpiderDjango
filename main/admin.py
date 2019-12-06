from django.contrib import admin
from . import models
# Register your models here.


class ReadAdmin(admin.ModelAdmin):
    list_display = ('sensorinstance', 'date', 'field1', 'field2', 'field3')

class ValueAdmin(admin.ModelAdmin):
    list_display = ('read' , 'value')

class CurrentMovementAdmin(admin.ModelAdmin):
    list_display = ('robot' , 'direction')

class PastMovementAdmin(admin.ModelAdmin):
    list_display = ('robot' , 'direction' , 'runtime_date' , 'duration')

class SensorInstanceAdmin(admin.ModelAdmin):
    list_display = ('pk','robot' , 'sensor')

admin.site.register(models.Robot)
admin.site.register(models.Sensor)
admin.site.register(models.Read, ReadAdmin)

admin.site.register(models.CurrentMovement, CurrentMovementAdmin)
admin.site.register(models.PastMovement, PastMovementAdmin)
admin.site.register(models.SensorInstance, SensorInstanceAdmin)
