# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_feedback_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
