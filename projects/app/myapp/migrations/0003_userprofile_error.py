# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20160323_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='error',
            field=models.CharField(default="User profile doesn't exist!", max_length=200),
        ),
    ]
