# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 12:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160308_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 8, 12, 10, 36, 931945), verbose_name='date modified'),
        ),
        migrations.AlterField(
            model_name='subquestion',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 8, 12, 10, 36, 970552), verbose_name='date modified'),
        ),
    ]
