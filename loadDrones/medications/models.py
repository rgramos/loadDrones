import re
from django.db import models
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from drones.models import Drone
from load_drones.models import AbsSlugTimestamp


def validation_name(value):
    if re.match("^([A-Za-z0-9])+([A-Za-z0-9_-])*$", value):
        raise ValidationError(_(f'{value} is incorrect, allowed only letters, numbers, ‘-‘, ‘_’.'))


def validation_code(value):
    if re.match("^([A-Z0-9])+([A-Z0-9_])*$", value):
        raise ValidationError(_(f'{value} is incorrect, allowed only upper case letters, underscore and numbers);'))


class Medication(AbsSlugTimestamp):
    name = models.CharField(validators=[validation_name], max_length=250)
    weight = models.FloatField()
    code = models.CharField(validators=[validation_code], max_length=250)
    image = models.ImageField()
    load = models.ManyToManyField(Drone, through='LoadMedicationDrone', blank=True, null=True)


class LoadMedicationDrone(AbsSlugTimestamp):
    medication = models.ForeignKey(Medication, verbose_name=_('Medication'), on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone, verbose_name=_('Drone'), on_delete=models.CASCADE)
    delivered_medication = models.DateTimeField(verbose_name=_('Initial Date'), editable=True, blank=True, null=True)
