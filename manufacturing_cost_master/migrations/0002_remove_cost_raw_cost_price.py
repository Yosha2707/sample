# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing_cost_master', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cost',
            name='raw_cost_price',
        ),
    ]
