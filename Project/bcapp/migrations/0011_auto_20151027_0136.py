# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bcapp', '0010_student_num_of_pref'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'username', max_length=100)),
                ('password', models.CharField(default=b'password', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='login',
            field=models.ForeignKey(to='bcapp.User', null=True),
        ),
    ]
