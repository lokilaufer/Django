# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


class MeasurementListCreateView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
