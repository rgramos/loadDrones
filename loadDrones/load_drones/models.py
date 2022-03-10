import uuid

from django.db import models
from django.utils import timezone


class AbsSlugTimestamp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(editable=False,
                                   default=timezone.now)
    updated = models.DateTimeField(editable=False,
                                   default=timezone.now)

    class Meta:
        abstract = True
