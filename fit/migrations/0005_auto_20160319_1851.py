# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0004_remove_dish_diet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dishdiet',
            name='diet',
        ),
        migrations.RemoveField(
            model_name='dishdiet',
            name='dish',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.RemoveField(
            model_name='user',
            name='favourite_diet',
        ),
        migrations.DeleteModel(
            name='Diet',
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.DeleteModel(
            name='DishDiet',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
