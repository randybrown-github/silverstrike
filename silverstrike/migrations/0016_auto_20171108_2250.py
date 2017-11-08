# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('silverstrike', '0015_importconfiguration_dateformat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurringtransaction',
            name='recurrence',
            field=models.IntegerField(choices=[(0, 'Disabled'), (1, 'Weekly'), (2, 'Monthly'), (3, 'Yearly')]),
        ),
    ]