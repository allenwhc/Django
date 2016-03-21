# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 10:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('user_create_date', models.DateTimeField(default=datetime.datetime(2016, 3, 16, 10, 55, 2, 323551), verbose_name='date created')),
                ('user_last_login_date', models.DateTimeField(verbose_name='date last login')),
            ],
        ),
        migrations.AddField(
            model_name='information',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.User'),
        ),
    ]