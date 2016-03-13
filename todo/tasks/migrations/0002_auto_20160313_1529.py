# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 15:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 3, 13, 15, 29, 37, 821796, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
    ]