# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cleaning',
            name='day',
        ),
        migrations.AddField(
            model_name='cleaning',
            name='collect_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
