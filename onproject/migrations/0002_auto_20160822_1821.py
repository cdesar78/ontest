# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-22 18:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('onproject', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 22, 18, 21, 8, 864785, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]
