from django.db import models

from core.models import TimeStamp


class Clinic(TimeStamp):
    id          = models.CharField(max_length=16, primary_key=True, db_index=True)
    name        = models.CharField(max_length=128)
    duration    = models.CharField(max_length=16, null=True)
    scope       = models.CharField(max_length=16, null=True)
    type        = models.CharField(max_length=16, null=True)
    institution = models.CharField(max_length=32, null=True)
    trial       = models.CharField(max_length=32, null=True)
    subjects    = models.PositiveIntegerField(null=True)
    department  = models.CharField(max_length=32, null=True)
    is_active   = models.BooleanField(default=True)

    class Meta:
        db_table = "clinics"
