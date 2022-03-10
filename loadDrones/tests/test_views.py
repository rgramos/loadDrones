from django.test import TestCase

from drones.models import Drone
from medications.models import Medication


class ViewsTest(TestCase):
    register_drone_data = {
        "serial_number": "QWERTY10",
        "model": Drone.CRUISERWEIGHT,
        "weight_limiter": "255",
        "battery_capacity": "100",
    }

    def setUp(self):
        self.drone = Drone.objects.create(serial_number='QWERTY10', model=Drone.MIDDLEWEIGHT, weight_limiter=255,
                                          battery_capacity=100, state=Drone.IDLE)
        self.medication = Medication.objects.create(name='Aspirin', code='QWE10', weight=101)
        self.load_drone = {
            "drone": self.drone.id,
            "medications": [self.medication.id]
        }

    def test_register_drone(self):
        response = self.client.post('/drones/register/', follow=True, data=self.register_drone_data)
        self.assertEqual(response.status_code, 201)

    def test_check_loaded_drones(self):
        response = self.client.get(f'/drones/check-loaded-drone/{self.drone.id}/',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_check_available_drones(self):
        response = self.client.get('/drones/check-available-drones/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_check_drone_battery_level(self):
        response = self.client.get(f'/drones/check-drone-battery/{self.drone.id}/',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_load_medication(self):

        response = self.client.post('/drones/load-medication-drone/', data=self.load_drone,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
