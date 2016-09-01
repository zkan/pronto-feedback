from __future__ import unicode_literals

from django.db import models


class Metric(models.Model):
    name = models.CharField(blank=True, max_length=50)
