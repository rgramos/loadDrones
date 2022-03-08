from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import GenericViewSet

from drones.models import Drone
from drones.serializers import DroneSerializer


class RegisterDroneViewSet(GenericViewSet, CreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
