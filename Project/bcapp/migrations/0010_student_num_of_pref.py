# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bcapp', '0009_auto_20151025_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Num_of_pref',
            field=models.IntegerField(default=1),
        ),
    ]
