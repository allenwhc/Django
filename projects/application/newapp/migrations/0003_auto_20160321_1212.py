# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 12:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20160316_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='birth_date',
            field=models.DateField(default=None, verbose_name='birthday'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 21, 12, 12, 32, 909438), verbose_name='date created'),
        ),
    ]