# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 01:39
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('feedback', '0002_auto_20160826_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
