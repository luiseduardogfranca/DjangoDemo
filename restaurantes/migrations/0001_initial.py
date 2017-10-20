# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200)),
                ('name', models.TextField()),
                ('speciality', models.CharField(max_length=200)),
                ('fund_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
