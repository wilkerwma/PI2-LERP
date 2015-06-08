# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=30)),
                ('state_of_success', models.BooleanField()),
                ('time_of_cleaning', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sensor_low', models.CharField(max_length=30)),
                ('sensor_mid', models.CharField(max_length=30)),
                ('sensor_high', models.CharField(max_length=30)),
                ('sensor_floor', models.CharField(max_length=30)),
                ('time_of_colect', models.CharField(max_length=100)),
                ('colect_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
