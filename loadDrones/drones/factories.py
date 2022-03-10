from factory.django import DjangoModelFactory

from drones.models import Drone


class DroneFactory(DjangoModelFactory):
    class Meta:
        model = Drone
