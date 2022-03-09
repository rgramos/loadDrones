from random import randint

from django.db import transaction
from django.core.management.base import BaseCommand

from drones.factories import DroneFactory
from drones.models import Drone
from medications.factories import MedicationFactory
from medications.models import Medication


DRONES_SIZE = 10
MEDICATIONS_SIZE = 10

medications_names_list = [
    'Abelbax',
    'Alglugine',
    'Oxycosin',
    'Desoprofen',
    'Toletisol',
    'Azelatamine',
    'Estroramine Doctospan',
    'Spirovital Crifase',
    'Atomomine Pralicelex',
    'Invanavir Alvidenu'
]

drone_model_choices = [item[0] for item in Drone.MODEL_CHOICE]
drone_state_choices = [item[0] for item in Drone.STATE_CHOICE]


class Command(BaseCommand):
    help = "Load Required Data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting previous data!")
        models = [Drone, Medication]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Loading new data!")
        for i in range(0, DRONES_SIZE):
            DroneFactory(
                serial_number=f"{randint(11111, 99999)}",
                model=drone_model_choices[randint(0, len(drone_model_choices) - 1)],
                weight_limiter=randint(1, 500),
                battery_capacity=randint(1, 100),
                state=drone_state_choices[randint(0, len(drone_state_choices) - 1)],
            )
        for i in range(0, MEDICATIONS_SIZE):
            MedicationFactory(
                name=medications_names_list[randint(0, len(medications_names_list) - 1)],
                weight=randint(1, 500),
                code=randint(1, 100),
                image='/image/pills-tamhsc.jpg',
            )
