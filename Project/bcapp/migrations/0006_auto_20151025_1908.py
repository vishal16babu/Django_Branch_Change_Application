# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bcapp', '0005_auto_20151025_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('preference', models.CharField(default=b'1', max_length=9, choices=[(b'1', b'AE B.Tech'), (b'2', b'CE B.Tech'), (b'3', b'CH'), (b'4', b'CL B.Tech'), (b'5', b'CL Dual Deg'), (b'6', b'CS B.Tech'), (b'7', b'EE B.Tech'), (b'8', b'EE Dual Deg E1'), (b'9', b'EE Dual Deg E2'), (b'10', b'EN Dual Deg'), (b'11', b'EP B.Tech'), (b'12', b'EP Dual Deg N1'), (b'13', b'ME B.Tech'), (b'14', b'ME Dual Deg M2'), (b'15', b'MM B.Tech'), (b'16', b'MM Dual Deg Y1'), (b'17', b'MM Dual Deg Y2')])),
                ('student', models.ForeignKey(to='bcapp.Person')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='student',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
