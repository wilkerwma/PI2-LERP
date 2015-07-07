# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150608_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='collect_date',
        ),
        migrations.AddField(
            model_name='history',
            name='collect_time',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='collect_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
