# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Site_value',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Date')),
                ('A_value', models.DecimalField(verbose_name=b'A Value', max_digits=5, decimal_places=2)),
                ('B_value', models.DecimalField(verbose_name=b'B Value', max_digits=5, decimal_places=2)),
                ('site_name', models.ForeignKey(verbose_name=b'Site', to='myapp.Site')),
            ],
        ),
    ]
