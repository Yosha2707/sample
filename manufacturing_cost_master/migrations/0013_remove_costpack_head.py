# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-28 10:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturing_cost_master', '0012_costpack_head'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costpack',
            name='Head',
        ),
    ]
