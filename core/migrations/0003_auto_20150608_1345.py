# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150607_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='time_of_colect',
            new_name='time_of_collect',
        ),
    ]
