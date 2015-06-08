# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150608_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='colect_date',
            new_name='collect_date',
        ),
        migrations.RemoveField(
            model_name='history',
            name='time_of_collect',
        ),
    ]
