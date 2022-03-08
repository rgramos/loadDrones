from django.db.migrations import state
from rest_framework.generics import CreateAPIView, RetrieveAPIView, get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drones.models import Drone
from drones.serializers import DroneSerializer, DroneCheckSerializer, DroneAvailableSerializer


class RegisterDroneViewSet(GenericViewSet, CreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


class CheckLoadedMedicationsItem(GenericViewSet, RetrieveAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneCheckSerializer

    def retrieve(self, request, *args, **kwargs):
        drone = self.get_object()
        if drone.state != Drone.LOADED:
            return Response({'message': 'Drone not loaded'})
        return super(CheckLoadedMedicationsItem, self).retrieve(self)


class CheckAvailableDrones(GenericViewSet, ListAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneAvailableSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(state=Drone.IDLE)




