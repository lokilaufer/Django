from django.urls import path
from django.urls import path, include
from rest_framework import routers
from .views import SensorListCreateView, MeasurementListCreateView, SensorUpdateView

# router = routers.DefaultRouter()
# router.register()

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensors'),
    path('sensors/<int:pk>/', SensorUpdateView.as_view(), name='sensor_detail'),
    path('measurements/', MeasurementListCreateView.as_view(), name='measurements')
]
