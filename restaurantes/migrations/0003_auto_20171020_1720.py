# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0002_auto_20171020_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='fund_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
