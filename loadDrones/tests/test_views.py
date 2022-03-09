from django.test import TestCase

from drones.models import Drone
from medications.models import Medication
from tests.factories import DroneFactory, MedicationFactory
from rest_framework.test import APIClient


class ViewsTest(TestCase):
    register_drone_data = {
        "id": "6dc381f330374602a25f002a383fe921",
        "serial_number": "QWERTY10",
        "model": "Cruiserweight",
        "weight_limiter": "255",
        "battery_capacity": "100",
    }

    load_drone = {
        "medications": ["1aac4ea3f6a542b99ede3999f71b78f0"],
        "drone": "6dc381f330374602a25f002a383fe921"
    }

    def setUp(self):
        self.drone = Drone.objects.create(id='6dc381f330374602a25f002a383fe921', serial_number='QWERTY10', model='Lightweight', weight_limiter=255,
                                          battery_capacity=100, state='IDLE')
        self.medication = Medication.objects.create(id='1aac4ea3f6a542b99ede3999f71b78f0', name='Aspirin', code='QWE10', weight=101)
        self.drone_load_medication_data = {
            "drone": self.drone.id,
            "medications": [self.medication.id]
        }

    def test_register_drone(self):
        response = self.client.post('/drones/register/', follow=True, data=self.register_drone_data)
        self.assertEqual(response.status_code, 201)

    def test_check_loaded_drones(self):
        response = self.client.get('/drones/check-loaded-drone/6dc381f330374602a25f002a383fe921/',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_check_available_drones(self):
        response = self.client.get('/drones/check-available-drones/', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_check_drone_battery_level(self):
        response = self.client.get('/drones/check-drone-battery/6dc381f330374602a25f002a383fe921/',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_load_medication(self):
        response = self.client.post('/drones/load-medication-drone/', data=self.load_drone,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
