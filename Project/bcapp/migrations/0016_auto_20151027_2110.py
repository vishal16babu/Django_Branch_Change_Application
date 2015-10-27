# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bcapp', '0015_indexes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='Num_of_pref',
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.CharField(default=b'150050049', max_length=9),
        ),
    ]
