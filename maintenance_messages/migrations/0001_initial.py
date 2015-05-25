# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance_Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=1000)),
                ('start_date', models.DateTimeField(verbose_name=b"message's start date")),
                ('end_date', models.DateTimeField(verbose_name=b"message's end date")),
                ('create_date', models.DateTimeField(verbose_name=b'creation date')),
            ],
        ),
    ]
