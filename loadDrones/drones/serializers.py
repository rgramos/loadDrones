from rest_framework import serializers

from drones.models import Drone
from medications.models import Medication


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        exclude = ('state',)


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        exclude = ('created', 'updated', 'load')


class DroneCheckSerializer(serializers.ModelSerializer):
    loaded_medications = MedicationSerializer(source='get_medication', many=True)

    class Meta:
        model = Drone
        fields = ('loaded_medications',)


class DroneAvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        exclude = ('created', 'updated')


class DroneBatteryLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ('battery_capacity',)
