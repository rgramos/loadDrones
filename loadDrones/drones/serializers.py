from django.db import transaction
from django.db.models import Sum
from rest_framework import serializers
from rest_framework.fields import ListField
from rest_framework.relations import PrimaryKeyRelatedField

from drones.models import Drone
from medications.models import Medication, LoadMedicationDrone


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


class LoadingDroneMedicationSerializer(serializers.Serializer):
    drone = PrimaryKeyRelatedField(queryset=Drone.objects.all())
    medications = ListField(child=PrimaryKeyRelatedField(queryset=Medication.objects.all()), min_length=1)

    @transaction.atomic()
    def create(self, validated_data):
        drone = validated_data.get('drone')
        for medication in validated_data.get('medications'):
            LoadMedicationDrone.objects.create(
                drone=drone,
                medication=medication
            )

        drone.state = Drone.LOADING
        drone.save()

        return Drone

    def validate(self, attrs):
        drone_max_weight = Drone.objects.get(id=attrs['drone'].id).weight_limiter
        medications_max_weight = 0
        for medication in attrs['medications']:
            medications_max_weight += medication.weight

        if drone_max_weight < medications_max_weight:
            raise serializers.ValidationError({
                'weight': f'The weight of medications is grater than drone capacity.'
            })

        if attrs['drone'].battery_capacity < 25:
            raise serializers.ValidationError({
                'battery_capacity': f'Drone battery is to low, the minimum battery is 25.'
            })

        if attrs['drone'].state != Drone.IDLE:
            raise serializers.ValidationError({
                'state': f'The Drone is busy.'
            })

        return super(LoadingDroneMedicationSerializer, self).validate(attrs)

