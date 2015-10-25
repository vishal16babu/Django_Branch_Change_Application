# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bcapp', '0008_auto_20151025_1919'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Student',
        ),
    ]
