# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bcapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_number', models.IntegerField(default=150050049)),
                ('name', models.CharField(max_length=200)),
                ('present_branch', models.TextField(verbose_name=b'None')),
                ('CPI', models.DecimalField(max_digits=3, decimal_places=2)),
                ('category', models.CharField(default=b'1', max_length=9, choices=[(b'1', b'GE'), (b'2', b'SC')])),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
