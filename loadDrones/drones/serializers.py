from rest_framework import serializers

from drones.models import Drone


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        exclude = ('state',)

