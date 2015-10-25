# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bcapp', '0007_auto_20151025_1917'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preference',
            old_name='preference',
            new_name='branch',
        ),
    ]
