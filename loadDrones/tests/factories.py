import factory

from drones.models import Drone
from medications.models import Medication


class DroneFactory(factory.Factory):
    class Meta:
        model = Drone

    id = '6dc381f330374602a25f002a383fe921'
    serial_number = '101010'
    model = 'Heavyweight'
    weight_limiter = 155
    battery_capacity = 100,
    state = 'IDLE'


class MedicationFactory(factory.Factory):
    class Meta:
        model = Medication

    id = '1aac4ea3f6a542b99ede3999f71b78f0'
    name = '789456'
    code = '10XD10'
    weight = 234
    image = 'media/images/medication/pills-tamhsc.jpg'
