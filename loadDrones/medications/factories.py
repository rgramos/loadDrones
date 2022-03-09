from factory.django import DjangoModelFactory

from medications.models import Medication


class MedicationFactory(DjangoModelFactory):
    class Meta:
        model = Medication
