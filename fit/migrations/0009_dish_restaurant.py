# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0008_remove_dish_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ManyToManyField(to='fit.Restaurant'),
        ),
    ]
