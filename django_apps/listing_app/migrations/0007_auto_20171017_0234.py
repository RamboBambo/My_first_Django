# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 02:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing_app', '0006_auto_20171016_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 17, 2, 34, 29, 384059)),
        ),
    ]
