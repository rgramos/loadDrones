from django.db import models
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from load_drones.models import AbsSlugTimestamp


def validate_weight_limiter(value):
    if value > 500:
        raise ValidationError(_(f'{value} is to much weight, 500 gr is the maximum load'))


def validate_battery_capacity(value):
    if value > 100:
        raise ValidationError(_(f'{value} is to much battery, 100 is the maximum value'))


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
    weight_limiter = models.FloatField(validators=[validate_weight_limiter])
    battery_capacity = models.IntegerField(validators=[validate_battery_capacity])
    model = models.CharField(max_length=255, choices=MODEL_CHOICE)
    state = models.CharField(max_length=255, choices=STATE_CHOICE, default=IDLE)

    class Meta:
        db_table = 'drone'
        verbose_name = 'Drone'
        verbose_name_plural = 'Drones'

    def __str__(self):
        return self.serial_number

    def get_medication(self):
        return self.medication_set.filter(loadmedicationdrone__delivered_medication=None)


class BatteryHistoryLevel(models.Model):
    drone = models.ForeignKey(Drone, verbose_name='drone', on_delete=models.CASCADE)
    battery_capacity = models.IntegerField(_("Battery capacity"), default=100)
    date = models.DateTimeField(_("Date"), auto_now_add=True)

    class Meta:
        db_table = "tbl_history_battery_level"
        verbose_name = "BatteryHistoryLevel"
        verbose_name_plural = "BatteryHistoryLevel"

