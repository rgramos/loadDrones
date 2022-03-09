from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drones.models import Drone
from drones.serializers import DroneSerializer, DroneCheckSerializer, DroneAvailableSerializer, \
    DroneBatteryLevelSerializer, LoadingDroneMedicationSerializer
from medications.models import LoadMedicationDrone


class RegisterDroneViewSet(GenericViewSet, CreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class CheckLoadedMedicationsItemViewSet(GenericViewSet, RetrieveAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneCheckSerializer

    def retrieve(self, request, *args, **kwargs):
        drone = self.get_object()
        if drone.state != Drone.LOADED:
            return Response({'message': 'Drone not loaded'})
        return super(CheckLoadedMedicationsItemViewSet, self).retrieve(self)


class CheckAvailableDronesViewSet(GenericViewSet, ListAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneAvailableSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(state=Drone.IDLE)


class CheckDroneBatteryLevelViewSet(GenericViewSet, RetrieveAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneBatteryLevelSerializer


class LoadingDroneViewSet(GenericViewSet, CreateAPIView):
    queryset = LoadMedicationDrone.objects.all()
    serializer_class = LoadingDroneMedicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = {
            'message': 'Successfully loaded drone'
        }
        return Response(response, status=status.HTTP_201_CREATED)
