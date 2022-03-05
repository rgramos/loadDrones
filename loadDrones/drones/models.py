from django.db import models

from loadDrones.models import AbsSlugTimestamp


class Drone(AbsSlugTimestamp):
    LIGHTWEIGHT = 'Lightweight'
    MIDDLEWEIGHT = 'Middleweight'
    CRUISERWEIGHT = 'Cruiserweight'
    HEAVYWEIGHT = 'Heavyweight'
    MODEL_CHOICE = [
        (LIGHTWEIGHT, 'Lightweight'),
        (MIDDLEWEIGHT, 'Middleweight'),
        (CRUISERWEIGHT, 'Cruiserweight'),
        (HEAVYWEIGHT, 'Heavyweight')
    ]

    IDLE = 'IDLE'
    LOADING = 'LOADING'
    LOADED = 'LOADED'
    DELIVERING = 'DELIVERING'
    DELIVERED = 'DELIVERED'
    RETURNING = 'RETURNING'
    STATE_CHOICE = [
        (IDLE, 'IDLE'),
        (LOADING, 'LOADING'),
        (LOADED, 'LOADED'),
        (DELIVERING, 'DELIVERING'),
        (DELIVERED, 'DELIVERED'),
        (RETURNING, 'RETURNING')
    ]

    serial_number = models.CharField(max_length=100)
    weight_limiter = models.FloatField()
    battery_capacity = models.IntegerField()
    model = models.CharField(max_length=255, choices=MODEL_CHOICE)
    state = models.CharField(max_length=255, choices=STATE_CHOICE)

    class Meta:
        db_table = 'drone'
        verbose_name = 'Drone'
        verbose_name_plural = 'Drones'

    def __str__(self):
        return self.serial_number
