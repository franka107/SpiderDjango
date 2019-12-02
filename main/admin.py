from django.contrib import admin
from . import models
# Register your models here.


class ReadAdmin(admin.ModelAdmin):
    list_display = ('robot', 'sensor', 'date')

class ValueAdmin(admin.ModelAdmin):
    list_display = ('read' , 'value')

admin.site.register(models.Robot)
admin.site.register(models.Sensor)
admin.site.register(models.Read, ReadAdmin)
admin.site.register(models.Value, ValueAdmin)
admin.site.register(models.Current_movement)
admin.site.register(models.Past_movement)
