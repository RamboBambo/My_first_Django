# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 23:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing_app', '0005_listing_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 16, 23, 41, 47, 996598)),
        ),
    ]