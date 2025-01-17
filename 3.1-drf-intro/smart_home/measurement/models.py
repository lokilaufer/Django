from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
from django.db import models


class Sensor(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, models.CASCADE, related_name='measurements')
    temperature = models.FloatField('Температура')
    created_at = models.DateTimeField('Дата и время измерения', auto_now=True)
