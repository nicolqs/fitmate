# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 19:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0007_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dish',
            name='restaurant',
        ),
    ]
