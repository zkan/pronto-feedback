# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_auto_20160827_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='last_modification_date',
        ),
    ]
