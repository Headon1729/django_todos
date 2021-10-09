from django.db import models
from datetime import datetime
from django.utils import timezone
from django.db.models.enums import Choices
import uuid
# Create your models here.

PRIORITIES = (('P1', 'MAJOR'), ('P2', 'NEUTRAL'), ('P3', 'MINOR'))


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, null=False, blank=False,)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    priority = models.CharField(max_length=2, choices=PRIORITIES, default='P1')

    def __str__(self):
        return self.title
