from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    title = models.TextField()
    category = models.CharField(max_length=50)
