from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Feedback(models.Model):
    fid = models.CharField(max_length=50)
    creation_date = models.DateTimeField(
        default=timezone.now,
        blank=True
    )
    last_modification_date = models.DateTimeField(
        default=timezone.now,
        blank=True
    )
    question_asked = models.TextField()
    message = models.TextField()
