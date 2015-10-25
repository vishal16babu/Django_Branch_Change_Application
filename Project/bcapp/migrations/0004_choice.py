# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bcapp', '0003_auto_20151025_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preference', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('student', models.ForeignKey(to='bcapp.Person')),
            ],
        ),
    ]
